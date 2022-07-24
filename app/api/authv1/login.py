from api import basic_auth
from authv1 import auth
from utils.decode_request import decode_request
from flask import Flask, request, render_template, redirect, current_app
from flask_cors import cross_origin
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies
)
from datetime import timedelta
import json
from models import User
from database import db


@basic_auth.verify_password
def verify_password(email, password):
    user = db.session.query(User).filter_by(email=email).scalar()

    if not user or not user.check_password(password):
        return None

    return user

@auth.route('/login', methods=['POST'])
@basic_auth.login_required
@cross_origin(supports_credentials=True)
def login():
    user = basic_auth.current_user()
    request_dic = request.get_json()

    if user is None:
        logger = current_app.logger
        logger.error('Wrong ID or password')
        import create_response

        content = json.dumps({'message': 'ID もしくは パスワードに誤りがあります。'})
        status_code = 401

        response = create_response.create_response(content, status_code)

        return response


    import create_response

    status_code = 200

    content = user.to_json()
    response = create_response.create_response(content, status_code)

    access_token = create_access_token(identity=user.id, expires_delta=timedelta(
        minutes=15), fresh=timedelta(minutes=15))
    set_access_cookies(response, access_token)

    try:
        if request_dic['remember'] == 1:
            refresh_token = create_refresh_token(identity=user.id)
            set_refresh_cookies(response, refresh_token)
    except KeyError:
        pass
    except TypeError:
        pass

    return response

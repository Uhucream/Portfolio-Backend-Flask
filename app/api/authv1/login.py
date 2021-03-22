from authv1 import auth
from flask import Flask, request, render_template, redirect, jsonify
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

@auth.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def login():
  raw_request_data = request.get_data()
  charset = request.mimetype_params.get('charset') or 'UTF-8'
  request_dic = json.loads(raw_request_data.decode(charset, 'replace'))

  user = db.session.query(User).filter_by(email=request_dic['email']).first()

  if not user or not user.check_password(request_dic['password']):
    import create_response

    content = json.dumps({'message': 'ID もしくは パスワードに誤りがあります。'})
    status_code = 401
    mimetype = 'application/json;charset=UTF-8'
    response = create_response.create_response(content, status_code, mimetype)

    return response
  else:
    import create_response

    status_code = 200
    mimetype = 'application/json;charset=UTF-8'
    content = user.to_json()
    response = create_response.create_response(content, status_code, mimetype)

    access_token = create_access_token(identity=user.id, expires_delta=timedelta(minutes=15), fresh=timedelta(minutes=15))
    print(access_token)
    set_access_cookies(response, access_token, max_age=timedelta(minutes=15))

    try:
      if request_dic['remember'] == 1:
        refresh_token = create_refresh_token(identity=user.id)
        set_refresh_cookies(response, refresh_token)
    except KeyError:
      pass

    return response
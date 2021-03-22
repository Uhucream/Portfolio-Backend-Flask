from authv1 import auth
from flask import Flask, request, render_template, redirect
from flask_cors import cross_origin
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    verify_jwt_in_request
)
import json
from api import jwt
from models import User, BlockedTokens
from database import db


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
  jti = jwt_payload['jti']
  token = db.session.query(BlockedTokens.id).filter_by(jti=jti).scalar()
  return token is not None


@auth.route('/protected', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required(fresh=True)
def protected():

    import create_response

    current_user = get_jwt_identity()
    content = json.dumps({"message": "Success", "logged_in_as": current_user})
    status_code = 200
    mimetype = 'application/json;charset=UTF-8'
    response = create_response.create_response(content, status_code, mimetype)

    return response

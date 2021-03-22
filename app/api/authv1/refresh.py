from authv1 import auth
from flask import Flask, request, render_template, redirect, jsonify
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    create_access_token,
    set_access_cookies
)
from models import User
from database import db
import json

@auth.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
  current_user_id = get_jwt_identity()
  access_token = create_access_token(identity = current_user_id)
  
  import create_response

  status_code = 200
  mimetype = 'application/json;charset=UTF-8'
  content = json.dumps({'is_success': True})
  response = create_response.create_response(content, status_code)

  set_access_cookies(response, access_token)

  return response

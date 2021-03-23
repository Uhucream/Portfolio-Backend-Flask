from authv1 import auth
from flask import Flask, request, render_template, redirect, jsonify
from flask_cors import cross_origin
from flask_jwt_extended import (
  get_jwt,
  jwt_required,
  unset_jwt_cookies,
  unset_access_cookies,
  unset_refresh_cookies
)
import json
from models import User, BlockedTokens
from database import db

@auth.route('/logout', methods=['DELETE'])
@cross_origin(supports_credentials=True)
@jwt_required()
def logout():

  import create_response

  response = jsonify({"message": "logout successful"})
  unset_jwt_cookies(response)

  jti = get_jwt()["jti"]
  db.session.add(BlockedTokens(jti=jti))
  db.session.commit()

  return response

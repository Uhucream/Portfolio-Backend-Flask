from apiv1 import api
from api.decode_request import decode_request
from flask import Flask, request, render_template, redirect
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
import json
from models import DailyReports
from database import db


@api.route('/submit_post', methods=['POST'])
@cross_origin(supports_credentials=True)
@jwt_required(fresh=True)
def submit_post():

    request_dic = decode_request(request)

    post_content = DailyReports(
        request_dic['title'], request_dic['body_text'])
    db.session.add(post_content)
    db.session.commit()

    result_dict = post_content.to_dict()

    import create_response
    response_json = json.dumps(result_dict, ensure_ascii=False)
    content = response_json
    status_code = 200

    response = create_response.create_response(content, status_code)

    return response

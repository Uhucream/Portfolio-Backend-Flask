from apiv1 import api
from utils.decode_request import decode_request
from utils.cut_none_keys import cut_none_keys
from flask import request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
import json
from models import MyWorks
from database import db
import create_response


@api.route('/my_works/submit', methods=['POST'])
# @cross_origin(supports_credentials=True)
# @jwt_required(fresh=True)
def submit_work():

    request_dic = decode_request(request)

    try:
        name = request_dic['name']
    except KeyError:
        content = json.dumps({'message': 'Work name is required'})
        status_code = 400

        response = create_response.create_response(content, status_code)

        return response

    try:
        end_point_uri = request_dic['end_point_uri']  # 成果物にアクセスする際に必要なエンドポイントを格納
    except KeyError:
        content = json.dumps({'message': 'end_point_uri is required'})
        status_code = 400

        response = create_response.create_response(content, status_code)

        return response

    try:
        description = request_dic['description']
    except KeyError:
        content = json.dumps({'message': 'Work description is required'})
        status_code = 400

        response = create_response.create_response(content, status_code)

        return response

    try:
        top_page_outline = request_dic['top_page_outline']
    except KeyError:
        content = json.dumps({'message': 'top_page_outline is required'})
        status_code = 400

        response = create_response.create_response(content, status_code)

        return response

    try:
        work_url = request_dic['work_url']
    except KeyError:
        work_url = None
        pass

    try:
        work_picture_url = request_dic['work_picture_url']
    except KeyError:
        work_picture_url = None
        pass

    new_content_dict = {
        'name': name,
        'end_point_uri': end_point_uri,
        'top_page_outline': top_page_outline,
        'description': description,
        'work_url': work_url,
        'work_picture_url': work_picture_url,
    }

    work_content = MyWorks(**new_content_dict)
    db.session.add(work_content)
    db.session.commit()

    result_dict = work_content.to_dict()

    import create_response
    response_json = json.dumps(result_dict, ensure_ascii=False)
    content = response_json
    status_code = 200
    response = create_response.create_response(content, status_code)

    return response

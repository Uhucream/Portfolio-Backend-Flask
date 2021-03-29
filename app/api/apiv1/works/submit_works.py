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
@cross_origin(supports_credentials=True)
@jwt_required(fresh=True)
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
        endpoint_uri = request_dic['endpoint_uri']  # 成果物にアクセスする際に必要なエンドポイントを格納
    except KeyError:
        content = json.dumps({'message': 'endpoint_uri is required'})
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
        id = request_dic['id']
    except KeyError:
        id = None
        pass

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
        'endpoint_uri': endpoint_uri,
        'top_page_outline': top_page_outline,
    }

    optional_args_dict = {
        'id': id,
        'work_url': work_url,
        'work_picture_url': work_picture_url,
        'description': description
    }

    cut_none_keys(optional_args_dict)

    work_content = MyWorks(**new_content_dict, **optional_args_dict)
    db.session.add(work_content)
    db.session.commit()

    result_dict = work_content.to_dict()

    import create_response
    response_json = json.dumps(result_dict, ensure_ascii=False)
    content = response_json
    status_code = 200
    response = create_response.create_response(content, status_code)

    return response

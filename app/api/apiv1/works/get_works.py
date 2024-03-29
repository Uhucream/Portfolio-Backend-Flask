from apiv1 import api
from flask import request
import json
from models import MyWorks
from database import db
import create_response


@api.route('/my_works', methods=['GET'])
def get_all_works():

    records_list = MyWorks.query.all()

    if len(records_list) == 0:
        content = json.dumps({'message': 'No Works Found'})
        status_code = 404
        mimetype = 'application/json;charset=UTF-8'
        response = create_response.create_response(
            content, status_code, mimetype)

        return response

    converted_records_list = list(map(lambda record: record.to_dict(), records_list))

    content = json.dumps(converted_records_list, ensure_ascii=False)
    status_code = 200
    mimetype = 'application/json;charset=UTF-8'
    response = create_response.create_response(
        content, status_code, mimetype)

    return response


@api.route('/my_work/<endpoint_uri>', methods=['GET'])
def get_one_work(endpoint_uri=None):

    record = MyWorks.query.filter_by(endpoint_uri=endpoint_uri).scalar()

    if record is None:
        response_json = json.dumps({'message': 'Not Found'})
        content = response_json
        status_code = 404
        mimetype = 'application/json;charset=UTF-8'
        response = create_response.create_response(
            content, status_code, mimetype)

        return response

    result_dict = record.to_dict()

    content = json.dumps(result_dict, ensure_ascii=False)
    status_code = 200
    mimetype = 'application/json;charset=UTF-8'
    response = create_response.create_response(
        content, status_code, mimetype)

    return response

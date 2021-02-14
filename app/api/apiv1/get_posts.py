from apiv1 import api
from flask import Flask, request, render_template, redirect
import json
from models import DailyReports
from database import db


@api.route('/posts', methods=['GET'])
def get_all_posts():

    record_list = DailyReports.query.all()

    if len(record_list) == 0:
        response_json = json.dumps({'message': 'No Posts Found'})
        import create_response
        content = response_json
        status_code = 404
        mimetype = 'application/json;charset=UTF-8'
        response = create_response.create_response(
            content, status_code, mimetype)

        return response
    else:
        dict_list = []
        for elem in record_list:
            raw_dict = elem.__dict__
            raw_dict.pop('_sa_instance_state')
            raw_dict['uuid'] = str(raw_dict['uuid'])
            raw_dict['created_at'] = raw_dict['created_at'].isoformat()
            raw_dict['updated_at'] = raw_dict['updated_at'].isoformat()
            dict_list.append(raw_dict)

        response_json = json.dumps(dict_list, ensure_ascii=False)
        import create_response
        content = response_json
        status_code = 200
        mimetype = 'application/json;charset=UTF-8'
        response = create_response.create_response(
            content, status_code, mimetype)

        return response


@api.route('/post/<id>', methods=['GET'])
def get_one_post(id=None):

    record_list = DailyReports.query.filter_by(id=id).all()

    if len(record_list) == 0:
        response_json = json.dumps({'message': 'Not Found'})
        import create_response
        content = response_json
        status_code = 404
        mimetype = 'application/json;charset=UTF-8'
        response = create_response.create_response(
            content, status_code, mimetype)

        return response
    else:
        result_dict = record_list[0].__dict__
        result_dict.pop('_sa_instance_state')
        result_dict['uuid'] = str(result_dict['uuid'])
        result_dict['created_at'] = result_dict['created_at'].isoformat()
        result_dict['updated_at'] = result_dict['updated_at'].isoformat()

        response_json = json.dumps(result_dict, ensure_ascii=False)
        import create_response
        content = response_json
        status_code = 200
        mimetype = 'application/json;charset=UTF-8'
        response = create_response.create_response(
            content, status_code, mimetype)

        return response

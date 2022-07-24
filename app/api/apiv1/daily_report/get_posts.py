from apiv1 import api
from flask import Flask, request, render_template, redirect
import json
from models import DailyReports
from database import db
import create_response


@api.route('/posts', methods=['GET'])
def get_all_posts():

    record_list = DailyReports.query.all()

    if len(record_list) == 0:
        content = json.dumps({'message': 'No Posts Found'})
        status_code = 404

        response = create_response.create_response(
            content, status_code)

        return response
    else:
        converted_records_list = list(map(lambda record: record.to_dict(), record_list))

        content = json.dumps(converted_records_list, ensure_ascii=False)
        status_code = 200

        response = create_response.create_response(
            content, status_code)

        return response


@api.route('/post/<id>', methods=['GET'])
def get_one_post(id=None):

    record = DailyReports.query.filter_by(id=id).scalar()

    if record is None:
        response_json = json.dumps({'message': 'Not Found'})
        content = response_json
        status_code = 404

        response = create_response.create_response(
            content, status_code)

        return response
    else:
        result_dict = record.to_dict()

        content = json.dumps(result_dict, ensure_ascii=False)
        status_code = 200

        response = create_response.create_response(
            content, status_code)

        return response

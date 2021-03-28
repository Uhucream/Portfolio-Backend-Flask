from apiv1 import api
from api.decode_request import decode_request
from flask import request, current_app
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
import json
from datetime import datetime, timedelta
from models import DailyReports
from database import db
import create_response


@api.route('/delete_post', methods=['DELETE'])
@cross_origin(supports_credentials=True)
@jwt_required(fresh=True)
def delete_post():
    request_data_dic = {}
    if request.args.get('id') is not None:
        request_data_dic['id'] = request.args.get('id')

    if request.args.get('uuid') is not None:
        request_data_dic['uuid'] = request.args.get('uuid')

    delete_content = db.session.query(DailyReports).filter(
        DailyReports.id == request_data_dic['id'], DailyReports.uuid == str(request_data_dic['uuid']))
    if delete_content.scalar() is None:
        content = json.dumps({'message': 'Not found reports'})
        status_code = 404

        response = create_response.create_response(
            content, status_code)

        return response

    else:
        delete_content.delete()
        db.session.commit()

        db.session.execute(
            "ALTER SEQUENCE daily_reports_id_seq RESTART WITH 1;")
        db.session.execute(
            "UPDATE daily_reports SET id=nextval('daily_reports_id_seq');")

        db.session.commit()

        content = json.dumps({'message': 'Success'})
        status_code = 204

        response = create_response.create_response(
            content, status_code)

        return response

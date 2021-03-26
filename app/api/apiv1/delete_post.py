from apiv1 import api
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
    request_data_json = request.get_json()
    
    delete_content = db.session.query(DailyReports).filter(DailyReports.id==request_data_json['id'], DailyReports.uuid==str(request_data_json['uuid']))
    if delete_content.scalar() is None:
      content = json.dumps({'message': 'Not found reports'})
      status_code = 404
      mimetype = 'application/json;charset=UTF-8'
      response = create_response.create_response(content, status_code, mimetype)

      return response

    else:
      delete_content.delete()
      db.session.commit()

      db.session.execute("ALTER SEQUENCE daily_reports_id_seq RESTART WITH 1;")
      db.session.execute("UPDATE daily_reports SET id=nextval('daily_reports_id_seq');")

      db.session.commit()

      content = json.dumps({'message': 'Success'})
      status_code = 204
      mimetype = 'application/json;charset=UTF-8'
      response = create_response.create_response(content, status_code, mimetype)

      return response

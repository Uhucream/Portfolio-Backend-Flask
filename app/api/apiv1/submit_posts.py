from apiv1 import api
from flask import Flask, request, render_template, redirect
import json
from models import models
from database import db


@api.route('/submit_post', methods=['POST'])
def submit_post():

    raw_request_data = request.get_data()
    charset = request.mimetype_params.get('charset') or 'UTF-8'
    request_dic = json.loads(raw_request_data.decode(charset, 'replace'))

    post_content = models.DailyReports(
        request_dic['title'], request_dic['body_text'])
    db.session.add(post_content)
    db.session.commit()
    
    result_dict = post_content.to_dict()
    result_dict['uuid'] = str(result_dict['uuid'])
    result_dict['created_at'] = result_dict['created_at'].isoformat()
    result_dict['updated_at'] = result_dict['updated_at'].isoformat()

    import create_response
    response_json = json.dumps(str(result_dict), ensure_ascii=False)
    content = response_json
    status_code = 200
    mimetype = 'application/json;charset=UTF-8'
    response = create_response.create_response(content, status_code, mimetype)

    return response


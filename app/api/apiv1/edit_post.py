from apiv1 import api
from flask import request, current_app
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
import json
from models import DailyReports
from database import db
import create_response


@api.route('/edit_post', methods=['PATCH'])
@cross_origin(supports_credentials=True)
@jwt_required(fresh=True)
def edit_post():
    logger = current_app.logger
    request_data_json = request.get_json()
    try:
        edit_target_id = str(request_data_json['id'])
        edit_target_uuid = str(request_data_json['uuid'])
    except KeyError:
        logger.info('A uuid and id of editing target is required.')
        content = json.dumps({'messages': 'A uuid and id of editing target is required.'})
        status_code = 400
        mimetype = 'application/json;charset=UTF-8'
        response = create_response.create_response(content, status_code, mimetype)

        return response

    try:
        edit_target_body = request_data_json['body_text']
    except KeyError:
        edit_target_body = None

    try:
        edit_target_title = request_data_json['title']
    except KeyError:
        edit_target_title = None


    if edit_target_title is None and edit_target_body is None:
        logger.info(
            'At least either \'title\' or \'body_text\' must be included')
        content = json.dumps({'messages': 'At least either \'title\' or \'body_text\' must be included'})
        status_code = 400
        mimetype = 'application/json;charset=UTF-8'
        response = create_response.create_response(content, status_code, mimetype)

        return response

    else:
        edit_content = db.session.query(DailyReports).filter(
            DailyReports.id == edit_target_id, DailyReports.uuid == edit_target_uuid)
        if edit_content.scalar() is None:
            logger.error('Not found reports')
            content = json.dumps({'message': 'Not found reports'})
            status_code = 404
            mimetype = 'application/json;charset=UTF-8'
            response = create_response.create_response(content, status_code, mimetype)

            return response
        else:
            update_dict = {
                'title': edit_target_title,
                'body_text': edit_target_body
            }

            edit_content_dict = edit_content.scalar().to_dict()
            original_content_dict = {
                'title': edit_content_dict['title'],
                'body_text': edit_content_dict['body_text']
            }

            for key in list(update_dict):
                if update_dict[key] is None:
                    update_dict.pop(key)
                    original_content_dict.pop(key)

            update_diffs_dict = dict(update_dict.items() - original_content_dict.items())

            if len(update_diffs_dict) == 0:
                logger.info('There are no changes')
                content = json.dumps({'message': 'There are no changes.'})
                status_code = 204
                mimetype = 'application/json;charset=UTF-8'
                response = create_response.create_response(content, status_code, mimetype)

                return response

            else:
                diff_results_list = []
                for diff_key in list(update_diffs_dict):
                    diff_result_dict = {
                        'column_name': diff_key,
                        'before_modified': original_content_dict[diff_key],
                        'after_modified': update_dict[diff_key]
                    }
                    diff_results_list.append(diff_result_dict)
                    
                logger.info(diff_results_list)

                try:
                  update_dict[DailyReports.title] = update_dict.pop('title')
                except KeyError:
                  pass

                try:
                  update_dict[DailyReports.body_text] = update_dict.pop('body_text')
                except KeyError:
                  pass

                edit_content.update(update_dict)
                db.session.commit()

                response_dict = {'message': 'Success',
                                 'diffs': diff_results_list}

                content = json.dumps(response_dict, ensure_ascii=False)
                status_code = 200
                mimetype = 'application/json;charset=UTF-8'
                response = create_response.create_response(
                    content, status_code, mimetype)

                return response

from apiv1 import api, db_connection, cursor
from flask import Flask, request, render_template, redirect
import psycopg2.extras
import json
 

@api.route('/posts', methods=['GET'])
def get_all_post():

  with db_connection as connection:
    with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM daily_reports;")
        row = cur.fetchall()
        result_list = []
        for item in row:
            result_list.append(dict(item))

    if len(result_list) == 0:
        response_json = json.dumps({'message': 'Not Found'})
        import create_response
        content = response_json
        status_code = 404
        mimetype = 'application/json'
        response = create_response.create_response(
            content, status_code, mimetype)

        return response
    else:
        final_result_list = []
        for dic in result_list:
            id_value = dic['id']
            dic.pop('id')
            final_result_list.append((id_value, dic))

        result_dict = dict(final_result_list)
        for dic in result_dict:
            result_dict[dic]['created_at'] = str(
                result_dict[dic]['created_at'])
            result_dict[dic]['updated_at'] = str(
                result_dict[dic]['updated_at'])

        response_json = json.dumps(result_dict)
        import create_response
        content = response_json
        status_code = 200
        mimetype = 'application/json'
        response = create_response.create_response(
            content, status_code, mimetype)

        return response


@api.route('/post/<id>', methods=['GET'])
def get_one_post(id=None):

    with db_connection as connection:
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT * FROM daily_reports WHERE id = '{}';".format(id))
            row = cur.fetchall()
            result_list = []
            for item in row:
                result_list.append(dict(item))

    if len(result_list) == 0:
        response_json = json.dumps({'message': 'Not Found'})
        import create_response
        content = response_json
        status_code = 404
        mimetype = 'application/json'
        response = create_response.create_response(
            content, status_code, mimetype)

        return response
    else:
        result_dict = result_list[0]
        result_dict['created_at'] = str(result_dict['created_at'])
        result_dict['updated_at'] = str(result_dict['updated_at'])

        response_json = json.dumps(result_dict)
        import create_response
        content = response_json
        status_code = 200
        mimetype = 'application/json'
        response = create_response.create_response(
        content, status_code, mimetype)

        return response

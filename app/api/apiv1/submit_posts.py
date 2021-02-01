from apiv1 import api, db_connection, cursor
from flask import Flask, request, render_template, redirect, url_for
import json
from datetime import datetime
from psycopg2.extras import DictCursor


@api.route('/post_test', methods=['POST'])
def post_test():

    request_dic = json.loads(request.get_data())

    with db_connection as connection:
      with connection.cursor(cursor_factory=DictCursor) as cur:
        cur.execute(
        "INSERT INTO daily_reports (title, created_at, updated_at, body_text) VALUES ('{}', '{}', '{}', '{}');".format(request_dic['title'], str(datetime.now()), str(datetime.now()), request_dic['body_text']))
    connection.commit()

    with db_connection as connection:
      with connection.cursor(cursor_factory=DictCursor) as cur:
        cur.execute("SELECT * FROM daily_reports ORDER BY id DESC LIMIT 1;")
        row = cur.fetchall()
        result_list = []
        for item in row:
          result_list.append(dict(item))

    result_dict = result_list[0]
    result_dict['created_at'] = str(result_dict['created_at'])
    result_dict['updated_at'] = str(result_dict['updated_at'])

    import create_response
    response_json = json.dumps(result_dict)
    content = response_json
    status_code = 200
    mimetype = 'application/json'
    response = create_response.create_response(content, status_code, mimetype)

    return response


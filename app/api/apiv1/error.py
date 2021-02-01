from flask import render_template
import exceptions
from apiv1 import api
import create_response
import json

@api.app_errorhandler(500)
def validation_error(e):
    content = 'Internal Error Occurred'
    status_code = 500
    mimetype = 'application/json'
    response = create_response.create_response(content, status_code, mimetype)

    return response

@api.app_errorhandler(exceptions.InvalidUsage)
def parameter_error_exception(e):
    content = json.dumps(e.to_dict(), indent=2, ensure_ascii=False)
    status_code = e.status_code
    mimetype = 'application/json'
    response = create_response.create_response(content, status_code, mimetype)

    return response


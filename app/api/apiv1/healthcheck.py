from apiv1 import api
from flask import Flask, request, render_template, redirect
import json

@api.route('/healthcheck', methods=['GET'])
def healthcheck():
  response_json = json.dumps({'status': 'healthy'})

  import create_response
  content = response_json
  status_code = 200
  mimetype = 'application/json'
  response = create_response.create_response(content, status_code, mimetype)

  return response
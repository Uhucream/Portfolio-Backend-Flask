from flask import Flask
from flask_cors import CORS
import sys, os
from pathlib import *
sys.path.append('{}/api/apiv1'.format(Path.cwd()))
sys.path.append('{}/api'.format(Path.cwd()))
import config
from werkzeug.debug import DebuggedApplication

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.config[config_name])
    CORS(app)

    from apiv1 import api as apiv1_blueprint
    app.register_blueprint(apiv1_blueprint, template_folder='templates', url_prefix='/v1')

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    return app
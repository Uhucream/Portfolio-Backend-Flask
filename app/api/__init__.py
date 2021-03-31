from models import *
from werkzeug.debug import DebuggedApplication
from cli import user
import config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
import sys
import os
from pathlib import *
from flask_jwt_extended import JWTManager
from flask_httpauth import HTTPBasicAuth
sys.path.append('{}/cli'.format(Path.cwd()))
sys.path.append('{}/api'.format(Path.cwd()))
sys.path.append('{}/api/utils'.format(Path.cwd()))
sys.path.append('{}/api/apiv1'.format(Path.cwd()))
sys.path.append('{}/api/authv1'.format(Path.cwd()))
sys.path.append('{}/models'.format(Path.cwd()))
sys.path.append('{}/instance'.format(Path.cwd()))
sys.path.append('{}/database'.format(Path.cwd()))
jwt = JWTManager()
basic_auth = HTTPBasicAuth()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.config[config_name])

    app.cli.add_command(user.user_cli)

    CORS(app)
    from database import db
    db.init_app(app)
    Migrate(app, db)
    jwt.init_app(app)

    from apiv1 import api as apiv1_blueprint
    from authv1 import auth as authv1_blueprint
    app.register_blueprint(
        apiv1_blueprint, template_folder='templates', url_prefix='/v1')
    app.register_blueprint(
        authv1_blueprint, template_folder='templates', url_prefix='/auth')

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    return app

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
import sys, os
from pathlib import *
sys.path.append('{}/api/apiv1'.format(Path.cwd()))
sys.path.append('{}/api'.format(Path.cwd()))
sys.path.append('{}/models'.format(Path.cwd()))
sys.path.append('{}/instance'.format(Path.cwd()))
sys.path.append('{}/database'.format(Path.cwd()))
import config
from werkzeug.debug import DebuggedApplication
from models import *

def create_app(config_name):
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.config.from_object(config.config[config_name])
    CORS(app)
    from database import db
    db.init_app(app)
    Migrate(app, db)

    from apiv1 import api as apiv1_blueprint
    app.register_blueprint(apiv1_blueprint, template_folder='templates', url_prefix='/v1')

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    return app

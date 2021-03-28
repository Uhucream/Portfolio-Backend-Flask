from flask import Blueprint

api = Blueprint('apiv1', __name__)

import healthcheck

from daily_report import *
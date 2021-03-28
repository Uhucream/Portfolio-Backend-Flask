from flask import Blueprint

api = Blueprint('apiv1', __name__)

import healthcheck

from daily_report import get_posts
from daily_report import submit_posts
from daily_report import edit_post
from daily_report import delete_post
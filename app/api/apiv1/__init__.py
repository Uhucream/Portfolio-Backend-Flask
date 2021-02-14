from flask import Blueprint

api = Blueprint('apiv1', __name__)

import get_posts
import submit_posts
import healthcheck

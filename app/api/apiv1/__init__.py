from flask import Blueprint
# import psycopg2

api = Blueprint('apiv1', __name__)

import get_posts
import submit_posts
import healthcheck

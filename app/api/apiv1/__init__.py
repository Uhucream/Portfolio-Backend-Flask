from flask import Blueprint
import psycopg2

api = Blueprint('apiv1', __name__)

db_connection = psycopg2.connect(
    "host=db port=5432 dbname=dev user=dev password=pass")
cursor = db_connection.cursor()

import get_posts
import submit_posts

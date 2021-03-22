from flask import Blueprint

auth = Blueprint('authv1', __name__)

import login
import logout
import refresh
import protected
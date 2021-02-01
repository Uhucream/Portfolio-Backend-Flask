import os
import sys
import api

env_name = os.getenv('FLASK_CONFIG', 'default')
print(' * Running Environment: {}'.format(env_name))
app = api.create_app(env_name)

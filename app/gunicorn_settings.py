import os
import socket

bind = '0.0.0.0:{}'.format(str(os.getenv('PORT', 5000)))
workers = 1
accesslog = '-'

if str(os.getenv('FLASK_CONFIG')) == 'development':
    loglevel = 'debug'
    reload = True

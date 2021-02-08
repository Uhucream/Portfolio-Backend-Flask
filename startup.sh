#!/usr/bin/env bash

./init_db.sh
flask db migrate
flask db upgrade
gunicorn -c gunicorn_settings.py application:app
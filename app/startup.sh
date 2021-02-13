#!/usr/bin/env bash

/usr/src/app/migrate.sh
gunicorn -c gunicorn_settings.py application:app
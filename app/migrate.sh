#!/bin/bash

DIR="/usr/src/app/migrations"

if [ ! -d $DIR ]; then
  flask db init && flask db migrate
fi

flask db upgrade
#!/bin/bash

DIR="migrations"

if [ ! -d $DIR ]; then
  flask db init
fi
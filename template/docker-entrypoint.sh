#!/bin/bash

python manage.py makemigrations
python manage.py migrate auth
python manage.py makemigrations app
python manage.py migrate
python manage.py collectstatic --noinput > /dev/null

gunicorn PROJECTNAME.wsgi -w 2 -b 0.0.0.0:8001 -t 81240

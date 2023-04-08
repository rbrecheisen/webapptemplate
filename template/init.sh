#!/bin/bash

rm -r webapp/app/migrations/*
touch webapp/app/migrations/__init__.py

rm db.sqlite3

python manage.py makemigrations
python manage.py migrate
python manage.py load_courses

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', '', 'admin')" | python manage.py shell
echo "Successfully created super user \"admin\""

python manage.py runserver
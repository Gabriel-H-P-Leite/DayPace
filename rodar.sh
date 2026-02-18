#!/bin/bash
source ambientePython/bin/activate
cd backend/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

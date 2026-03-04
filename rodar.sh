#!/bin/bash
cd backend/
source ambientePython/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

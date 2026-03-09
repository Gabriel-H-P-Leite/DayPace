#!/bin/bash
cd backend/
source /home/gabriel/Documentos/Software/DayPace/ambientePython/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

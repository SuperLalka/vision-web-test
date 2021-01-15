#!/bin/bash
# pipenv shell

case $1 in
  start)
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata fixtures/data.json
    python manage.py runserver
    ;;
esac

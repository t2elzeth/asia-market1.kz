#!/bin/bash

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py initadmin

exec gunicorn -c "./gunicorn_config.py" core.wsgi

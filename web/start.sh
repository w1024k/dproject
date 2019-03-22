#!/bin/bash

echo start!

cd /root/dproject/wangyang/ &
python manage.py clearpyc &
python manage.py collectstatic --noinput &
python manage.py celery worker -l info -f /var/log/celery.log -D &
gunicorn -c wangyang/gunicorn.conf.py wangyang.wsgi:application
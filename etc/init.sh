#!/bin/bash

sudo cp /home/box/web/etc/django  /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-available/django /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart
# sudo /etc/init.d/gunicorn restart
# sudo /etc/init.d/mysql start

# вызвать команду в корне проекта, где находиться файл manage.py
# gunicorn ask.wsgi:application --bind 127.0.0.1:8000
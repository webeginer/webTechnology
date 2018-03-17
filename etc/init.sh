#!/bin/bash
sudo apt-get update
sudo rm /etc/nginx/sites-enabled/default
sudo ﻿cp /home/box/web/etc/django  /etc/nginx/sites-available/django
sudo ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart

# sudo /etc/init.d/gunicorn restart
# вызвать команду в корне проекта, где находиться файл manage.py
# gunicorn ask.wsgi:application --bind 127.0.0.1:8000

sudo /etc/init.d/mysql start
mysql -u root
# create database database_ask;
# alter database database_ask default character set utf8 collate utf8_unicode_ci;
# show databases; 
# create user 'vs'@'%';
# grant all privileges on *.* to 'vs'@'%';
# flush privileges;
# sudo ﻿ln -s /home/box/web/etc/mysqld.cnf /etc/mysql/my.cnf

# python manage.py check
# python manage.py makemigrations qa
# python manage.py migrate
# show tables in database_ask;
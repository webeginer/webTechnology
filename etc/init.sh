#!/bin/bash
# sudo apt-get update
# sudo apt-get upgrade
sudo rm /etc/nginx/sites-enabled/default
sudo ﻿cp /home/box/web/etc/django  /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart
# sudo /etc/init.d/gunicorn restart
# вызвать команду в корне проекта, где находиться файл manage.py
# python manage.py runserver 0.0.0.0:8000
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
# drop database database_ask;

# python manage.py check
# python manage.py makemigrations
# python manage.py migrate

# создать таблицу базы данных в качестве кэша с помощью следующей команды:
# python manage.py createcachetable
# show tables in database_ask;




#!/bin/bash

sudo mv /home/box/web/etc/reverseProxy  /etc/nginx/sites-available/default
sudo ln -s /etc/nginx/sites-available/reverseProxy /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
# sudo /etc/init.d/mysql start
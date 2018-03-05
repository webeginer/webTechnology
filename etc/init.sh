#!/bin/bash

sudo mv /home/box/web/etc/nginx.conf  /etc/nginx/sites-available/frontend
sudo ln -s /etc/nginx/sites-available/frontend /etc/nginx/sites-enabled/
sudo rm -rf /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart
# sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
# sudo /etc/init.d/gunicorn restart
# sudo /etc/init.d/mysql start
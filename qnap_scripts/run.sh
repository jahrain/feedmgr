#!/bin/sh

cd /share/CACHEDEV1_DATA/.qpkg/feedmgr/current
nohup ./env/bin/python manage.py runserver 0.0.0.0:8001 2>&1 >> /opt/var/feedmgr/log/feedmgr.log &

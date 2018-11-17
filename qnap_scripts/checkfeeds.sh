#!/bin/sh

cd /share/CACHEDEV1_DATA/.qpkg/feedmgr/current
nohup ./env/bin/python manage.py checkfeeds 2>&1 >> /opt/var/feedmgr/log/feedmgr_checkfeeds.log &

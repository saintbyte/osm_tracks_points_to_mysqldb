#!/bin/bash
if [ -f "nohup.out" ] ; then
echo "allready work"
exit 1
fi
nohup ./to_mysql.py simple-gps-points-120604.csv   &
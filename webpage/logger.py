#!/usr/local/bin/python
import time
from webpage import settings
from django.core.management import setup_environ
setup_environ(settings)
from monitor.models import DataPoint
from datetime import datetime

while True:
    with open('/baby/temperature') as f:
        temp = f.readline().strip()
    with open('/baby/humidity') as f:
        humidity = f.readline().strip()
    point = DataPoint(temp=float(temp), humidity=float(humidity))
    point.save()
    print "Temperature (%s) and humidity (%s) logged at %s" %\
            (temp, humidity, str(datetime.now()))
    time.sleep(5.0)

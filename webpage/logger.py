#!/usr/local/bin/python
import time
from webpage import settings
from django.core.management import setup_environ
setup_environ(settings)
from monitor.models import DataPoint
from datetime import datetime
import json
import re
import requests

counter = 0
digits = re.compile(r'\d+')
while True:
    # Log the temperature and humidity every five seconds
    if not counter % 10:
        with open('/baby/temperature') as f:
            temp = f.readline().strip()
        with open('/baby/humidity') as f:
            humidity = f.readline().strip()
        point = DataPoint(temp=float(temp), humidity=float(humidity))
        point.save()
        print "Temperature (%s) and humidity (%s) logged at %s" %\
                (temp, humidity, str(datetime.now()))

    # Check for the baby's cry twice a second
    with open('/baby/crying', 'r+') as f:
        data = f.read()
        if digits.match(data):
            payload = {'volume': data}
            requests.post('http://129.105.5.89/alert/', data=payload)
            print "Sent cry alert! Volume: %s" % data

            # Overwrite cry value; daemon will write new decibel value
            # if baby is still crying
            f.seek(0)
            f.write('False')

    counter += 1
    time.sleep(0.5)

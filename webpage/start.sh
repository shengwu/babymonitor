source '/usr/local/bin/virtualenvwrapper.sh'
workon baby
python /root/babymonitor/webpage/manage.py runserver_socketio 0.0.0.0:80

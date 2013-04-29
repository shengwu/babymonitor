from django_socketio import events, broadcast 
from monitor.models import Caretaker

@events.on_message
def message(request, socket, context, message):
	print "Server received a message"

@events.on_connect
def connect(request, socket, context):
	print "New connection established!"

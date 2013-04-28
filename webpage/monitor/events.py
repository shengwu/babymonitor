from django_socketio import events 

@events.on_message
def message(request, socket, context, message):
	print "Server received a message"
	socket.send({"message": "Server received your message"})

@events.on_connect
def connect(request, socket, context):
	socket.send({"message": "Connection Opened!"})


from django.http import HttpResponse
from django.shortcuts import render 
from django_socketio import broadcast, NoSocket

def home(request):
	try:
		broadcast({"message": "Someone is about to join us"})
	except NoSocket:
		print "Broadcast not sent: No connected sockets."
	return render(request, 'monitor/home.html', {})

def alert(request):
	print "Tear alert detected on server."
	try:
		broadcast({"message": "Dr. Orwell sayz: YOUR BABY IS PISSED. GO LOVE IT."})
	except NoSocket:
		print "Broadcast not sent: No connected sockets."
	return HttpResponse("We get it. you're crying. wa wa waaa")

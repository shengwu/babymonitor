from django.http import HttpResponse
from django.shortcuts import render 
from django_socketio import broadcast, NoSocket
from monitor.models import *

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

    # Record cry
    # Since they're based on claps, use all same fields for now
    # In the future, maybe send length/volume parameters in the URL
    cry = Cry()
    cry.length = 0.1 # in seconds
    cry.volume = 100 # in decibels
    cry.save()
    print "Cry recorded at %s" % cry.time
    return HttpResponse("We get it. you're crying. wa wa waaa")

def cries(request):
    return render(request, 'monitor/cries.html', 
            {'cries': Cry.objects.all()})

from django.http import HttpResponse
from django.shortcuts import render 
from django_socketio import broadcast, NoSocket
from monitor.models import *
import random

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
    cry.length = random.uniform(0.1, 3.0) # in seconds
    cry.volume = random.uniform(60, 110) # in decibels
    cry.save()
    print "Cry recorded at %s\nLength: %f\nVolume: %f" % \
        (cry.time, cry.length, cry.volume)
    return HttpResponse("We get it. you're crying. wa wa waaa")

def cries(request):
    return render(request, 'monitor/cries.html', 
            {'cries': Cry.objects.all()})

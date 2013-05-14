from django.http import HttpResponse
from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django_socketio import broadcast, NoSocket
from monitor.models import *
import json
import os
import random
import socket

@login_required
def home(request):
    try:
        broadcast({"message": "Someone is about to join us"})
    except NoSocket:
        print "Broadcast not sent: No connected sockets."

    # Read temperature and humidity
    with open('/baby/temperature') as f:
        temp = f.readline().strip()
    with open('/baby/humidity') as f:
        humidity = f.readline().strip()

    # Get current IP
    if os.name != "nt":
        import fcntl
        import struct
        def get_interface_ip(ifname):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, 
                       struct.pack('256s', ifname[:15]))[20:24])
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = ["eth0", "eth1", "eth2", "wlan0", "wlan1", "wifi0", 
                        "ath0", "ath1", "ppp0"]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass

    return render(request, 'monitor/home.html', {
        'temp': temp,
        'humidity': humidity,
        'ip_address': ip,
        })

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

@login_required
def cries(request):
    return render(request, 'monitor/cries.html', 
            {'cries': Cry.objects.all()})

@login_required
def users(request):
    if request.user.groups.filter(name='owner'):
        return render(request, 'monitor/users.html', {'users': User.objects.all().order_by('-is_active')})
    else:
        return render(request, 'monitor/denied.html', {})

@login_required
def options(request):
    if request.user.groups.filter(name='owner'):
        return render(request, 'monitor/options.html', {})
    else:
        return render(request, 'monitor/denied.html', {})


    return render(request, 'monitor/denied.html', {})

def modify_user(request):
    user = User.objects.get(id=request.POST['uid'])
    name = user.first_name
    if request.POST['action'] == 'delete':
        user.delete()
        return HttpResponse(name + " has been deleted")
    elif request.POST['action'] == 'activate':
        user.is_active = True
        user.save()
        return HttpResponse(name + " has been activated")
    elif request.POST['action'] == 'deactivate':
        user.is_active = False
        user.save()
        return HttpResponse(name + " has been deactivated")
    return HttpResponse("Invalid action")

def get_humidity_and_temp(request):
    # Read temperature and humidity
    with open('/baby/temperature') as f:
        temp = f.readline().strip()
    with open('/baby/humidity') as f:
        humidity = f.readline().strip()
    info = {'temp': temp, 'humidity': humidity}
    return HttpResponse(json.dumps(info), mimetype='application/json')

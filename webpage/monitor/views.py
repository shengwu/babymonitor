from django.http import HttpResponse
from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django_socketio import broadcast, NoSocket
from monitor.models import *
from .forms import UploadFileForm
import json
import os, subprocess, sys
import random
import socket

def check_owner(request):
    if not request.user.groups.filter(name='owner'):
        return render(request, 'monitor/denied.html', {})

def baby_render(request, url, dictionary):
    dictionary.update({'babies': Baby.objects.all()})
    if len(Baby.objects.all()) == 0:
        return create_baby(request)
    else:
        return render(request, url, dictionary)

def handle_uploaded_file(f):
    with open('/baby/audio/uploaded.wav', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    subprocess.Popen(["sudo", "-u", "curt", "cvlc", "/baby/audio/uploaded.wav"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def play_audio(request):
    return httpResponse("We played the file")

@login_required
def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print "HANDLING FORM"
            handle_uploaded_file(request.FILES['file'])

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

    # Write volume threshold
    with open('/baby/threshold', 'w') as f:
        f.write(str(Baby.objects.get(is_active=True).max_vol))

    return baby_render(request, 'monitor/home.html', {
        'temp': temp,
        'humidity': humidity,
        'ip_address': ip,
        'form': UploadFileForm(),
        })

def alert(request):
    print "Tear alert detected on server."
    try:
        broadcast({"message": "Dr. Orwell sayz: YOUR BABY IS PISSED. GO LOVE IT."})
    except NoSocket:
        print "Broadcast not sent: No connected sockets."

    # Record cry
    cry = Cry()
    cry.length = random.uniform(0.1, 3.0) # in seconds
    cry.volume = int(request.POST['volume'])
    cry.save()
    print "Cry recorded at %s\nLength: %f\nVolume: %f" % \
        (cry.time, cry.length, cry.volume)

    return HttpResponse("We get it. you're crying. wa wa waaa")

@login_required
def cries(request):
    return baby_render(request, 'monitor/cries.html', 
            {'cries': Cry.objects.all()})

@login_required
def users(request):
    check_owner(request)
    return baby_render(request, 'monitor/users.html', {'users': User.objects.all().order_by('-is_active')})

@login_required
def options(request):
    check_owner(request)
    if(request.POST):
        baby = Baby(name=request.POST['baby_name'])
        baby.save()
    return baby_render(request, 'monitor/options.html', {})

def modify_baby(request):
    baby = Baby.objects.get(pk=request.POST['baby_name'])
    value = float(request.POST['value'])
    field = request.POST['field']
    print "Modifying baby with field: " + field
    if(field == 'delete'):
        #baby.delete()
        print "DELETING BABY!!!"
        return HttpResponse("your baby has been deleted!")
    elif(field == 'max_vol'):
        baby.max_vol = value 
    elif(field == 'max_temp'):
        baby.max_temp = value
    elif(field == 'min_temp'):
        baby.min_temp = value
    elif(field == 'active'):
        Baby.objects.all().update(is_active = False)
        baby.is_active = True
    baby.save()

    # Write volume threshold
    with open('/baby/threshold', 'w') as f:
        f.write(str(Baby.objects.get(is_active=True).max_vol))

    return HttpResponse("your baby has been modified")

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

def play_audio(request):
    os.system("cvlc /home/curt/test.wav")
    return HttpResponse("We played your file!")

@login_required
def create_baby(request):
    check_owner(request)
    return baby_render(request, 'monitor/create_baby.html', {})

def get_humidity_and_temp(request):
    # Read temperature and humidity
    with open('/baby/temperature') as f:
        temp = f.readline().strip()
    with open('/baby/humidity') as f:
        humidity = f.readline().strip()
    info = {'temp': temp, 'humidity': humidity}

    return HttpResponse(json.dumps(info), mimetype='application/json')

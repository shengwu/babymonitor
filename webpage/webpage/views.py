from django.http import HttpResponse
from django.shortcuts import render 
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from monitor.models import *
from monitor.views import *

def login_view(request):
    if(request.user.is_authenticated()):
		return home(request) 
    if(not request.POST):
        return render(request, 'login.html', {'error_message': ''})
    
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password) 
    if(user is not None and user.is_active):
		login(request, user)
		return home(request)
    else:
        return render(request, 'login.html', {'error_message': 'Wrong email or password, you jerk.'})

def register(request):
    if(not request.POST):
	    return render(request, 'register.html', {'error_message': ''})

    username = request.POST['username']
    password = request.POST['password']	
    if(len(request.POST['name']) < 1):
        return render(request, 'register.html', {'error_message': 'We need your name, you fool of a Took.'})
    nameList = request.POST['name'].split(' ',1)
    firstname = nameList[0]
    lastname = ""
    if(len(nameList) > 1):
        lastname = nameList[1]
    # process the Password
    if(password != request.POST['repeat-password']):
        return render(request, 'register.html', {'error_message': 'Password does not match, you meanie.'})
    if(len(password) < 4):
        return render(request, 'register.html', {'error_message': 'Your password needs to be at least 4 characters, you inconsiderate twerp.'})
    try:
        user = User.objects.create_user(username=username, password=password, email=username, first_name=firstname, last_name=lastname)
    except IntegrityError:
        return render(request, 'register.html', {'error_message': 'That user name already exists, you poopoo head.'})
    if('owner' not in request.POST):
        user.is_active = False
        user.save()
        return render(request, 'login.html', {'error_message': 'Account created for ' + firstname + '. Have the monitor owner activate your account, you horse thief!'})
    else:
        user.groups.add(Group.objects.get(name='owner'))
        user.save()
        user = authenticate(username=username, password=password) 
        login(request, user)
        return home(request)

def logout_view(request):
    logout(request)
    return login_view(request)

def register_owner(request):
    logout(request)
    return render(request, 'register.html', {'owner': 'True'})

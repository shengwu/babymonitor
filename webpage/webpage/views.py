from django.http import HttpResponse
from django.shortcuts import render 
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from monitor.models import *

def login_view(request, message=''):
	return render(request, 'login.html', {'error_message': message})

def register(request, message=''):
	return render(request, 'register.html', {'error_message': message})

def logout_view(request):
	logout(request)
	return HttpResponse("You have logged out. Goodbye.")

def home(request):
	return render(request, 'monitor/home.html', {})

def auth(request):
	if(request.user.is_authenticated()):
		return home(request) 
	elif(not request.POST):
		return login_view(request, 'Please enter your credentials, you miscreant.')
	else:
		username = request.POST['username']
		password = request.POST['password']
		
		# if we are registering a new user
		if('repeat-password' in request.POST):
			if(password != request.POST['repeat-password']):
				return register(request, 'Password does not match, you meanie.')
			if(len(password) < 4):
				return register(request, 'Your password needs to be at least 4 characters, you inconsiderate twerp.')
			try:
				user = User.objects.create_user(username=username, password=password)
			except IntegrityError:
				return register(request, 'That user name already exists, you poopoo head.')
				user.is_active = False
				user.save()
			return login_view(request, 'Have the monitor owner activate your account, you horse thief!')
							
		# if we are just logging in
		else:
			user = authenticate(username=username, password=password) 
			if user is not None:
				if user.is_active:
					login(request, user)
					return home(request)
			return login_view(request, 'Wrong username or password, you jerk.')

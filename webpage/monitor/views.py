from django.http import HttpResponse
from django.shortcuts import render 

def home(request):
	print "Routing you to home!"
	return render(request, 'monitor/home.html', {})

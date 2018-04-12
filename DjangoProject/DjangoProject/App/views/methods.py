from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.core.mail import EmailMessage

def retrive(request):
	if request.user.is_authenticated:
		
	else:
    
	return HttpResponse()

def display(request):
	if request.user.is_authenticated:
		
	else:
    
	return HttpResponse()

def edit(request):
	if request.user.is_authenticated:
		
	else:
    
	return HttpResponse()

def delet(request):
	if request.user.is_authenticated:
		
	else:
    
	return HttpResponse()

def each_activity(request):
	if request.user.is_authenticated:
		
	else:
    
	return HttpResponse()

def retrive_each_stramwise(request):
	if request.user.is_authenticated:
		
	else:
    
	return HttpResponse()

def delete_each_streamwise(request):
	if request.user.is_authenticated:

	else:
    
	return HttpResponse()

def algo_for_best():
	if request.user.is_authenticated:

	else:

	return HttpResponse()

def create_csv(request):
		if request.user.is_authenticated:

	else:

	return HttpResponse()

def reduce_size_of_img(request):
	if request.user.is_authenticated:

	else:

	return HttpResponse()

def check_schedule(request):
	if request.user.is_authenticated:

	else:

	return HttpResponse()

def retrive_imges(request):
	if request.user.is_authenticated:

	else:

	return HttpResponse()

def make_csv(request):
	if request.user.is_authenticated:

	else:

	return HttpResponse()
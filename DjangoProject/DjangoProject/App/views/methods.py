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
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from DjangoProject.App.models import *

def ProUser(request):
    name = request.GET.get("dt1")
    activity = request.GET.get("dt2")
    print name,activity
    prouser_collection = connection.test.prouser.ProfessionalUser()
    prouser_collection['name'] = name
    prouser_collection['activity'] = activity
    prouser_collection.save()
    user_data = connection.test.prouser.ProfessionalUser.find()
    for each in user_data:
    	print each
    template = "prouser.html"
    return render(request,template)
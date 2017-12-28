from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.template import RequestContext
from DjangoProject.App.models import *


def User(request):
    name = request.POST.get('name')
    print name
    user_collection = connection.test.user.User()
    name = user_collection['name'] 
    # user_collection.save()
    user_data = connection.test.prouser.ProfessionalUser.find()
    for each in user_data:
    	print each

    	template = "user.html"
 #    	variable = RequestContext(request, {'user_data': user_data})
	# return render_to_response(template, variable)
	return render(request,template)

# def data(request):
# 	user_data = connection.test.user.User.find()
# 	return render_to_response(request,'data.html',{'user_data':user_data})


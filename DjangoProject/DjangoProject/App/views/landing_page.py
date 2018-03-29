from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext

def landing_page(request):
	a="ashutosh"
    return render_to_response('landing_page.html',
    {'a':a},context_instance=RequestContext(request))

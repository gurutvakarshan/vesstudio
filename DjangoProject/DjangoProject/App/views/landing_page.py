from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext

def landing_page(request):
    return render_to_response('landing_page.html',{},context_instance=RequestContext(request))

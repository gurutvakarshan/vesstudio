from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext

def landing_page(request):
    template = 'landing_page.html'
    return render(request,template)
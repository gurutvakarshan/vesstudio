from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from django.template import loader
from django.template import RequestContext
import gridfs
from pymongo import Connection
from DjangoProject.App.models import *
import base64
import magic
def User(request):
    if request.method == 'POST':
        my_uploaded_file = request.FILES['file']
        my_uploaded_file = my_uploaded_file.read()
        print type(my_uploaded_file) #print str
        print my_uploaded_file
        # my_uploaded_file = request.FILES['file'].read() #also work
        # print my_uploaded_file
        # for each in my_uploaded_file:
			# print "CHUNK:",each
    return render_to_response('user.html', {},context_instance=RequestContext(request))

def data(request):
    if request.method == 'POST':
    	title = request.POST.get("title")
    	source = request.POST.get("source")
    	template = request.POST.get("template")
        my_uploaded_file = request.FILES['file']
        read_file = my_uploaded_file.read()
    	# print type(my_uploaded_file)
    	
        instance = connection.test2.largefiles.StoreLargeFiles()
        instance['title'] = title
        instance.save()
        instance.fs.source = str(source)
        # instance.save()
        instance.fs.template = str(template)
        # instance.save()
        instance.fs.images[str(my_uploaded_file)] = read_file
        
        # instance.save() 
        # my_uploaded_file = request.FILES['file'].read() #also work
        # print my_uploaded_file
        # for each in my_uploaded_file.chunks():
			# print "CHUNK:",each
    return render_to_response('data.html',{},context_instance=RequestContext(request))

def retrive(request):
	instance = connection.test2
	Files = instance.fs.files.find()
	Chunks = instance.fs.chunks.find({},{"data":0})
	for each in Files:
		print "Files:",each																																																																																																																																																																																																																																																																																																																																																																																													
	for each in Chunks:
		print "Chunks:",each
	print "A:",instance.fs
	# for each in instance.fs.images.find({}):
	# 	print "each:",each
	return StreamingHttpResponse("")
	# return render_to_response('retrive.html',{},context_instance=RequestContext(request))

def showimg(request):
	a = []
	instance = connection.test2.largefiles.StoreLargeFiles()
	# for each in instance:																																																				
		# print each
	for f in instance.fs.images.find():
		de = f.read()
		print de
		html = "<video width='400' controls><source src='%s' type='mkv'></video>" %de
		# html = "<html><body><img src='%s' height='100' width='100'/></body></html>" % de
	# return HttpResponse(de,content_type="jpeg")
		# print f #<gridfs.grid_file.GridOut object at 0x7f51d36aca90>
		# b = f.read().decode('base64')
		# a.append(b)	
	# for each in a:
		# print "In A:",each
	# return render_to_response('show.html',{'de':de},context_instance=RequestContext(request),content_type="mp4")
	return HttpResponse(html,content_type='mkv')																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																															
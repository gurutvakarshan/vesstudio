from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.core.mail import EmailMessage
from DjangoProject.App.models import *

def forms(request):
	return render_to_response('forms_ui.html',{},context_instance=RequestContext(request))

def level1(request):
	if request.method == "POST":
		examination_passed = request.POST.get("exp")
		pass_year = request.POST.get("pass-year")
		total_mark = request.POST.get("total-mark")
		percentage = request.POST.get("percentage")
		rank = request.POST.get("rank")
	        
		level1_instance = connection.ves_dev.levels1.Level1()
		level1_instance['examination_passed'] = examination_passed
		level1_instance['yop'] = pass_year
		level1_instance['total_mark'] = total_mark
		level1_instance['percentage'] = percentage
		level1_instance['rank'] = rank
		level1_instance.save()
	return render_to_response('level1.html',{},context_instance=RequestContext(request))

def level2(request):
    if request.method== "POST":
    	selected_subcat = request.POST.get("selected-subcat")
    	year = request.POST.get("year")
    	event = request.POST.get("event")
    	description = request.POST.get("description")

    	level2_instance = connection.ves_dev.levels2.Level2()
    	level2_instance['selected_subcat'] = selected_subcat
    	level2_instance['year'] = year
    	level2_instance['event'] = event
    	level2_instance['description'] = description
    	level2_instance.save()    	
    return render_to_response('level2.html',{},context_instance=RequestContext(request))

def level3(request):
    if request.method== "POST":
    	selected_subcat = request.POST.get("selected-subcat")
    	year = request.POST.get("year")
    	event = request.POST.get("event")
    	description = request.POST.get("description")

    	level3_instance = connection.ves_dev.levels3.Level3()
    	level3_instance['selected_subcat'] = selected_subcat
    	level3_instance['year'] = year
    	level3_instance['event'] = event
    	level3_instance['description'] = description
    	level3_instance.save()    	
    return render_to_response('level3.html',{},context_instance=RequestContext(request))

def level4(request):
    if request.method== "POST":
    	selected_subcat = request.POST.get("selected-subcat")
    	year = request.POST.get("year")
    	event = request.POST.get("event")
    	description = request.POST.get("description")
     
        level4_instance = connection.ves_dev.levels4.Level4()
    	level4_instance['selected_subcat'] = selected_subcat
    	level4_instance['year'] = year
    	level4_instance['event'] = event
    	level4_instance['description'] = description
    	level4_instance.save() 	
    return render_to_response('level4.html',{},context_instance=RequestContext(request))

def level5(request):
    if request.method== "POST":
    	selected_subcat = request.POST.get("selected-subcat")
    	year = request.POST.get("year")
    	achievement = request.POST.get("achievement")
    	description = request.POST.get("description")
     
        level5_instance = connection.ves_dev.levels5.Level5()
    	level5_instance['selected_subcat'] = selected_subcat
    	level5_instance['year'] = year
    	level5_instance['achievement'] = event
    	level5_instance['description'] = description
    	level5_instance.save()    	
    return render_to_response('level5.html',{},context_instance=RequestContext(request))

def level6(request):
	if request.method== "POST":
		nss = request.POST.get("radio1")
		rotract_club = request.POST.get("radio2")
		llle = request.POST.get("radio3")
		acp = request.POST.get("radio4")
		others = request.POST.get("others")

		level6_instance = connection.ves_dev.levels6.Level6()
		level6_instance['nss'] = nss
		level6_instance['rotract_club'] = rotract_club
		level6_instance['llle'] = llle
		level6_instance['acp'] = acp
		level6_instance['others'] = others
		level6_instance.save()  	
	return render_to_response('level6.html',{},context_instance=RequestContext(request))

def schedule(request):
	if request.method == "POST":
		p1_start_dt = request.POST.get("p1_st_dt")
		p1_end_dt = request.POST.get("p1_end_dt")
		p2_start_dt = request.POST.get("p2_st_dt")
		p2_end_dt = request.POST.get("p2_end_dt")
		p3_start_dt = request.POST.get("p3_st_dt")
		p3_end_dt = request.POST.get("p3_end_dt")

		schedule_instance = connection.ves_dev.scheduleds.Scheduled()
		schedule_instance['p1_start_dt'] = p1_start_dt
		schedule_instance['p1_end_dt'] = p1_end_dt
		schedule_instance['p2_start_dt'] = p2_start_dt
		schedule_instance['p2_end_dt'] = p2_end_dt
		schedule_instance['p3_start_dt'] = p3_start_dt
		schedule_instance['p3_end_dt'] = p3_end_dt
		schedule_instance.save()
	return render_to_response('schedule.html',{},context_instance=RequestContext(request))
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.core.mail import EmailMessage
from DjangoProject.App.models import *

def registration(request):
    if request.method== "GET":
        role = request.GET.get("role")
        first_name = request.GET.get("first-name")
        last_name = request.GET.get("last-name")
        klass = request.GET.get("klass")
        roll_number = request.GET.get("roll-number")
        birth_date = request.GET.get("birth-date")
        telephone_number = request.GET.get("telephone-number")
        mobile_number = request.GET.get("mobile-number")
        address = request.GET.get("address")
        activity = request.GET.get("activity")
        email = request.GET.get("email")
        password = request.GET.get("password")
        user_member_reg = connection.ves_dev.contestants_reg.UserMemberReg()
    
        user_member_reg['role'] = role
        user_member_reg['first_name'] = first_name
        user_member_reg['last_name'] = last_name
        user_member_reg['klass'] = klass
        user_member_reg['roll_number'] = roll_number
        user_member_reg['birth_date'] = birth_date
        user_member_reg['telephone_number'] = telephone_number
        user_member_reg['mobile_number'] = mobile_number
        user_member_reg['address'] = address
    	# user_member_reg['activity'] = activity
        user_member_reg['email'] = email
        user_member_reg['password'] = password
        user_member_reg.save()
        activation_email(request,email)
        return render_to_response('member_registration.html',{},context_instance=RequestContext(request))
    else:
        pass
        

def adminjuryreg(request):
	if request.method== "POST":
		role2 = request.POST.get("role")
    	first_name = request.POST.get("first-name")
    	last_name = request.POST.get("last-name")
    	klass = request.POST.get("klass")
        roll_number = request.POST.get("roll-number")
        birth_date = request.POST.get("birth-date")
        # telephone_number = request.POST.get("telephone-number")
        mobile_number = request.POST.get("mobile-number")
        address = request.POST.get("address")
        activity = request.POST.get("activity")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_member_reg = connection.ves_dev.admins_juries_reg.Admin_Jury_Member_Reg()
    	user_member_reg['role'] = role2
    	user_member_reg['first_name'] = first_name
    	user_member_reg['last_name'] = last_name
    	user_member_reg['klass'] = klass
    	user_member_reg['roll_number'] = roll_number
    	user_member_reg['birth_date'] = birth_date
    	# user_member_reg['telephone_number'] = telephone_number
    	user_member_reg['mobile_number'] = mobile_number
    	user_member_reg['address'] = address
    	# user_member_reg['activity'] = activity
    	user_member_reg['email'] = email
    	user_member_reg['password'] = password
    	user_member_reg.save()
    	activation_email(request,email)
	return HttpResponse("/success_register_activation_mail_sent")
	
def member_login(request):
	if request.method =="POST":
		email = request.POST.get("email")
        password = request.POST.get("password")
        # connectivity
        user_member_reg = connection.ves_dev.contestants_reg.UserMemberReg.find({'email':email,'password':password})
        if user_member_reg:
   			member = authenticate(request,email=email,password=password)
   			if member is not None:
   				login(request,member)
   				return HttpResponseRedirect("/homepage")
   			else:
   				return HttpResponseRedirect("/invalid")

def member_logout(request):
	logout(request)
	return HttpResponseRedirect("/logout")

def activation(request):
	return HttpResponse("Your account is now activate.")

# def activation_email(request,email):
# 	host_name = request.META['HTTP_HOST']
# 	print "Host name:",host_name
# 	email_instance = EmailMessage('Activation Email Link','Please click the following likk below<br><a href="https://'+host_name+'/activation/complete">Activation Link.Please Click to Activate Account</a>',"repo.opensource@example.com",[email],headers={'Message-ID': 'foo'},)
#     if email_instance:
#         email_instance.send()
#         return HttpResponse("")
#     else:
#         pass

def verify_email_first(request):
	if request.method =="POST":
		verify_email_first = request.POST.get("verify_email_first","")
		user_member_reg = connection.ves_dev.contestants_reg.UserMemberReg.find({'email':verify_email_first})
		if user_member_reg:
			request.session['email'] = user_member_reg
			return HttpResponseRedirect("/reset_password_redirect")
		else:
			return HttpResponseRedirect("/no_email_found")

# def reset_password_later(request):
#     if request.method == "POST":
#         new_password = request.POST.get("new_password")
#         check_key = request.session.has_key('email')
#         if new_password and check_key:
#             session_email = request.session['email']
#             user_member_reg = connection.ves_dev.contestants_reg.UserMemberReg.update(
#                                                                                         {'email':session_email},
#                                                                                         {$set:{'password':new_password}}    
#                                                                                     )
#             return HttpResponseRedirect("/success_password")
# 		else:
# 			return HttpResponseRedirect("/sorry")
#     else:
#         return render_to_response('some_template',{},context_instance=RequestContext(request))

def success(request):
    template = "success.html"
    return render_to_response(template,{},context_instance=RequestContext(request))

def no_email_found(request):
    template = "no_email_found.html"
    return render_to_response(template,{},context_instance=RequestContext(request))

def reset_password_redirect(request):
    template = "no_email_found.html"
    return render_to_response(template,{},context_instance=RequestContext(request))

def invalid(request):
    template = "invalid.html"
    return render_to_response(template,{},context_instance=RequestContext(request))

def logout(request):
    template = "logout.html"
    return render_to_response(template,{},context_instance=RequestContext(request))

def success_register_activation_mail_sent(request):
    template = "success_register_activation_mail_sent.html"
    return render_to_response(template,{},context_instance=RequestContext(request))

def cache(request):
    template = "cache.html"
    return render_to_response(template,{},context_instance=RequestContext(request))   

def activation_template(request):
    template = "activation_template.html"
    return render_to_response(template,{},context_instance=RequestContext(request)) 
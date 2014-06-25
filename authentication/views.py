from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

def home(request):
	if request.user.is_authenticated():
		# return HttpResponseRedirect(reverse('football'))
		return HttpResponse('ts')
	return render_to_response('home.html', {}, context_instance=RequestContext(request))

def register(request):
	if request.method == 'POST':
		first_name = request.POST['fname']
		last_name = request.POST['lname']
		email = request.POST['email']
		password = request.POST['password']
		try:
			User.objects.get(email=email)
			return HttpResponse('User already exists')
		except User.DoesNotExist:
			user = User.objects.create_user(email, email, password)
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			return HttpResponseRedirect('/')
	return render_to_response('register.html', context_instance=RequestContext(request))

def user_login(request):
	email = request.POST['username']
	password = request.POST['password']
	user = authenticate(username='john', password='secret')
	if user is not None:
		if user.is_active:
		    return HttpResponseRedirect(reverse('games'))
		else:
		    return HttpResponse("The password is valid, but the account has been disabled!")
	else:
		print("The username and password were incorrect.")

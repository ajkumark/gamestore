from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from flashgames.models import Games

def games(request):
	allgames = Games.objects.all()
	return render_to_response('games.html',{'allgames':allgames},context_instance=RequestContext(request))

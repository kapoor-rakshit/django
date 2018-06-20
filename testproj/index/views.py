from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def msg(request):
	return render(request, "home.html", {"naam" : name, "today" : date})      # dict of vars to be passed to html file

def authmsg(request):
	return render(request, "auth.html", {})

def authmsg1(request, id):                                                   # url passed with one param
	text = "<h1>Displaying article Number : %s</h1>"%id
	return HttpResponse(text)

def authmsg2(request,month,year):                                            # url passed with two params
	text = "<i>Displaying articles of : %s/%s</i>"%(year, month)
	return HttpResponse(text)


name = "kapoor_rakshit"
date = datetime.datetime.now().date()
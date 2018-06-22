from django.shortcuts import render
from django.http import HttpResponse

from index.forms import LoginForm, SaveForm
from index.models import testdb

import datetime

# Create your views here.

def msg(request):
	return render(request, "home.html", {"naam" : name, "today" : date})      # dict of vars to be passed to html file

def authmsg(request):
	return render(request, "auth.html", {})

def readrec(request):
	name = ""
	roll = ""
	city = ""
	if request.method == "POST":                                           # handle POST request
		formdata = LoginForm(request.POST)

		if formdata.is_valid():                                           # data validation
			roll = (formdata.cleaned_data['roll'])
			name = (formdata.cleaned_data['name'])
			city = (formdata.cleaned_data['city'])
		else:
			return render(request, "auth.html", {"form" : formdata})

	else:
		formdata = LoginForm()                                           # handle other request with an empty form

	return render(request, "home.html", {"name" : name, "roll" : roll, "city" : city})

def saverec(request):
	entrieslist = []
	if request.method == "POST":
		formdata = SaveForm(request.POST)

		if formdata.is_valid():
			formdata.save()
			obj = testdb.objects.all()
			for item in obj:
				entrieslist.append(item)
		else:
			return render(request, "auth.html", {"form" : formdata})
	else:
		formdata = SaveForm()

	return render(request, "home.html", {"entries" : entrieslist})

def authmsg1(request, id):                                                   # url val passed with one param captured here
	text = "<html><body><h1>Displaying article Number : %s</h1></body></html>"%id
	return HttpResponse(text)

def authmsg2(request,month,year):                                            # url val(s) passed with two params captured here
	text = "<html><body><i>Displaying articles of : %s %s</i></body></html>"%(year, month)
	return HttpResponse(text)


name = "kapoor_rakshit"
date = datetime.datetime.now().date()
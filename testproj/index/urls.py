from django.urls import path, re_path
from django.views.generic import ListView
from index.models import testdb

from index import views

# To capture a value from the URL, use angle brackets.
# Captured values can optionally include a converter type. The default is a 'str' if a converter isn’t included in the expression.
# For example, <int:name>
#              <slug:st>   slug - Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters
# NOTE : var name must be same as arg passed to views.py func irrespective of order in which passed.

# In order to perform URL reversing, use named URL patterns (by specifying name arg in path() func)

# To use regular expressions. use re_path() instead of path().
# the syntax for named regular expression groups is auth/(?P<name>pattern)/
# eg : re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.year_archive)


urlpatterns = [
	 
	 path('home/', views.msg, name = 'msg'),

	 path('auth/', views.authmsg, name = 'auth'),

	 path('readrec/', views.readrec, name = 'disp'),

	 path('saverec/', views.saverec, name = 'save'),

	 path('disprec/', ListView.as_view(model = testdb, template_name = "home.html")),

	 path('auth/<int:id>/', views.authmsg1, name = 'oneparam'),                       

	 path('auth/<int:year>/<int:month>/', views.authmsg2, name = 'twoparams'),

]


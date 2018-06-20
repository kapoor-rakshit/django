from django.urls import path
from index import views

urlpatterns = [
	 
	 path('home/', views.msg, name = 'msg'),

	 path('auth/', views.authmsg, name = 'auth'),

	 path(r'auth/(\d+)/', views.authmsg1, name = 'oneparam'),                       # url with regex (r) to have one param

	 path(r'auth/(?P\d{2})/(?P\d{4})/', views.authmsg2, name = 'twoparams'),        # two params

]
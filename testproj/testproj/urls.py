"""testproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from index import views                                     # 1. import APP_NAME's views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.msg, name='msg'),                       # 1. (URLpath, VIEWpath, nameoffunc)    # '' (empty) - home

  # 2. ANOTHER WAY (considered best) : URLs of an app can be included at once with a separate urls.py file in app dir
  #    now accessible via 'index/home/' , 'index/auth/'   ...
    path('index/', include('index.urls')),                
]

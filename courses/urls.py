"""eMahei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import CategoriesListView


urlpatterns = [
    path('coursedetails/<int:id>', views.coursedetails, name='coursedetails'),
    path('allcourses/<int:id>', views.allcourses, name='allcourses'),
    path('video/', views.video, name='video'),
    #path(r'^coursedetails/(?P<id>[0-9]+)/$', views.coursedetails, name='coursedetails')
    #path('allcourses/<int:id>', views.CategoriesListView.as_view(), name='allcourses'),
   
   
    ] 

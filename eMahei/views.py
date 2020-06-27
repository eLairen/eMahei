from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm

from courses.models import Courses, Categories, Instructor

def eMahei(request):
    
    courses= Courses.objects.all()
    categories = Categories.objects.all()
    

   
    return render(request, "index.html",{'Courses':courses, 'cat_nav':categories});





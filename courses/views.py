from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.forms import inlineformset_factory
from django.views.generic import ListView


from django.contrib.auth.forms import UserCreationForm

from courses.models import Courses, Categories, Chapter, Topics, Instructor

# Create your views here.

def coursedetails(request, id=None):
    categories = Categories.objects.all()
     
    isinstance = get_object_or_404(Courses,pk=id)
   
    chapter1 = Chapter.objects.filter(course_name=isinstance).order_by('chapter_no')
    instructor = Instructor.objects.all()
    return render(request, "coursedetails.html", {'Courses':isinstance,
    'cat_nav':categories,
    'chapt': chapter1,
    'inst':instructor });

'''
class CategoriesListView(ListView):
    model = Categories
    template_name = "allcourses.html"

    def get_queryset(self):
        return Categories.objects.all()
'''


def allcourses(request,id):
    isinstance = get_object_or_404(Categories,pk=id)
    category = Categories.objects.all()
    courses = Courses.objects.filter(category_id=isinstance)

    return render(request, "allcourses.html",{'categories':isinstance, 'course':courses,'cat_nav': category});


def video(request):
    category = Categories.objects.all()
    return render(request, "mainvideo.html",{'cat_nav':category});

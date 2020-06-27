from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.forms import inlineformset_factory
from django.views.generic import ListView


from django.contrib.auth.forms import UserCreationForm

from courses.models import Categories
from blog.models import Blog, Blog_category

# Create your views here.

def blog_content(request):
    categories = Categories.objects.all()
    blog = Blog.objects.all()
    cont = Blog_category.objects.all()

    return render(request, "blog-content.html", {'cat_nav':categories, 'category': cont, 'bcont': blog});

def blog_cat(request,id):
    categories = Categories.objects.all()
    isinstance = get_object_or_404(Blog,pk=id)
    blog = Blog.objects.filter(title=isinstance)
    cont = Blog_category.objects.all()

    return render(request, "blog-content.html", {'cat_nav':categories, 'category': cont, 'bcont': blog});
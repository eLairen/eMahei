from tinymce.widgets import TinyMCE
from django.contrib import admin
from django.db import models


#Register your models here.
from .models import Blog, Blog_category

admin.site.register(Blog)
admin.site.register(Blog_category)
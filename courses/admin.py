from tinymce.widgets import TinyMCE
from django.contrib import admin
from django.db import models


#Register your models here.
from .models import Courses 
from .models import Categories
from .models import Language_name


from .models import Course_enroll_details
from .models import Chapter
from .models import Topics
from .models import Ebooks
from .models import Instructor
from .models import FAQ
from .models import Enotes

# Register your models here.


class MyAdmin(admin.ModelAdmin):
    menu_title = "Users"
    menu_group = "Staff"



class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'lastupdate','price','offer']
    list_filter = ['lastupdate','offer'] 
    search_fields = ['title','instructor__firstname']  
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
    
    fieldsets = (
        ('Course Name and Display', {
            'fields': ('title','subtitle','thumnail','category')
        }),
        ('Price Section', {
            'fields': ('price','offer','offerprice')
        }),        
        ('Details of the Course', {
            'fields': ('picture','language_name','instructor','durations', 'What_you_will_learn','requirments')
        }),
    ) 

class ChapterAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_name']
    list_filter = ['course_name']  

admin.site.register(Instructor)
admin.site.register(Categories)
admin.site.register(Language_name)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Topics)
admin.site.register(Ebooks)
admin.site.register(Course_enroll_details)
admin.site.register(FAQ)
admin.site.register(Enotes)










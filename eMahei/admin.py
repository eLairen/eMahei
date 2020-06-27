from django.contrib.auth.models import Group
from django.contrib import admin




admin.site.site_header = "eMahei Admin"
admin.site.site_title = "eMahei Admin Dashboard"
admin.site.index_title = "eMahei Admin Dashboard"

class MyAdmin(admin.ModelAdmin):
    menu_title = "Users"
    menu_group = "Staff"


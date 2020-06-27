from django.contrib import admin
# Register your models here.
from django.db import models
from .models import User_accounts

admin.site.register(User_accounts)
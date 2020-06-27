from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.



class User_accounts(models.Model):
    
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "username"
    def __str__(self):
        return str(self.username)




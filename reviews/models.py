
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from courses.models import Courses


# Create your models here.
class reviews_class(models.Model):
    RATING_CHOICES = ( 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5")
    ) 
    username = models.ForeignKey(User, related_name='Review_User', blank=True, null=True, on_delete=models.CASCADE)
    course_name = models.ForeignKey(Courses, related_name='Review_Courses',blank=True, null=True, on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now=True)
    rating = models.CharField( 
        max_length = 20, 
        choices = RATING_CHOICES, 
        default = '1')
    review = models.TextField()
    reply = models.TextField()
    class Meta:
        verbose_name_plural = "reviews"
    def __str__(self):
        return str(self.username)


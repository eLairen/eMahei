from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from courses.models import Courses

from courses.models import Chapter


# Create your models here.


class Discussion(models.Model):
    student_name = models.ForeignKey(User, related_name='User', blank=True, null=True, on_delete=models.CASCADE)
    course_name = models.ForeignKey(Courses, related_name='Courses', blank=True, null=True, on_delete=models.CASCADE)
    chapter_name = models.ForeignKey(Chapter, related_name='Chapter', blank=True, null=True, on_delete=models.CASCADE)
    topic =  models.CharField(max_length=500)
    discussion_text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.student_name)

class DiscussionReply(models.Model):
    discussion_name = models.ForeignKey(Discussion, related_name='Discussion', blank=True, null=True, on_delete=models.CASCADE)
    
    reply = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.discussion_name)


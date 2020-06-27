from django.db import models

# Create your models here.


class Blog_category(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Blog Category"
    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    author_picture = models.FileField(upload_to='author_pic/', null=True)
    about_author = models.TextField()
    category = models.ForeignKey(Blog_category, blank=True, null=True, on_delete=models.CASCADE)
    blog_image = models.FileField(upload_to='blog_pic/', null=True)
    article = models.TextField()
    date_of_publish = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Blog"
    def __str__(self):
        return self.title






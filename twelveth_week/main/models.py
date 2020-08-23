from django.db import models
from django.conf import settings
from account.models import CustomUser
# from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_at=models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comment(models.Model):
    objects = models.Manager()
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.content

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jasoseol(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    content = models.TextField()
    update_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    objects = models.Manager()
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Jasoseol, on_delete=models.CASCADE, null=True)
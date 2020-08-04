from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Blog(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
from django.db import models
from datetime import datetime

# Create your models here.

class myAlbum (models.Model):
    object = models.Manager()
    name = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    release = models.DateTimeField(default=datetime.now, blank=True)
    playTime = models.IntegerField()
    genre = models.TextField()
    albumArt = models.ImageField(upload_to="image", blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
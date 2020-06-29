from django.db import models

# Create your models here.

class myAlbum (models.Model):
    object = models.Manager()
    name = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    release = models.IntegerField()
    playTime = models.IntegerField()
    genre = models.TextField()
    albumArt = models.ImageField(upload_to="image", blank=True)
    desription = models.TextField()

    def __str__(self):
        return self.name
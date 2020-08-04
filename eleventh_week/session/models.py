from django.db import models

# Create your models here.

class Melon_list(models.Model):
    objects = models.Manager()
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    rank = models.IntegerField(default=0)
    img_src = models.TextField(blank=True)
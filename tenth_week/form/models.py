from django.db import models

# Create your models here.

class FirstModel(models.Model):
    x = (
        ('good', '좋아요'),
        ('bad', '싫어요'),
    )
    title = models.CharField(max_length=50)
    text = models.TextField()
    recommend = models.CharField(max_length=5, choices=x)
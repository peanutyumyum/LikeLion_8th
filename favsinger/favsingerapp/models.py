from django.db import models

# Create your models here.

class singer(models.Model):
    object = models.Manager()
    singerName = models.CharField(max_length=100, default="가수이름을 입력해주세요")
    favSongName1 = models.CharField(max_length=50, default="곡명을 입력해주세요")
    whyFavSinger = models.TextField(default="애정 이유는 뭔가요?")   

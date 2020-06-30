from django.db import models

# Create your models here.

class members(models.Model):
    objects = models.Manager()
    memberId = models.IntegerField(primary_key=True)
    memberName = models.CharField(max_length=127)
    home = models.CharField(max_length=1023)

class Orders(models.Model):
    objects = models.Manager()
    memberId = models.ForeignKey(members ,on_delete = models.SET_NULL, null=True, blank=True)
    orderId = models.IntegerField(primary_key=True)
    
class Goods(models.Model):
    objects = models.Manager()
    goodsName = models.CharField(max_length=127)
    goodsId = models.IntegerField(primary_key=True)
    goodsPrice = models.IntegerField(max_length=30)

class Sheets(models.Model):
    objects = models.Manager()
    memberId = models.ForeignKey(members ,on_delete = models.SET_NULL, null=True, blank=True)
    goodsId = models.ForeignKey(Goods ,on_delete = models.SET_NULL, null=True, blank=True)
    orderId = models.ForeignKey(Orders ,on_delete = models.SET_NULL, null=True, blank=True)

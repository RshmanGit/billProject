from __future__ import unicode_literals

from django.db import models

# Create your models here.
class order(models.Model):
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    quantity = models.IntegerField()
    order_date = models.DateField()
    delivery_date = models.DateField()
    delivered = models.BooleanField(default = False)
    
    def __str__():
        return '%s %s %d' % (self.name, self.village)
    
class rawMaterialOrder(models.Model):
    
    gatePass = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    weight = models.IntegerField()
    order_date = models.DateField()
    delivery_date = models.DateField()
    recieved = models.BooleanField(default = False)
    
    def __str__():
        return '%d %s %s' % (self.gatePass, self.name, self.desc)
    
class expenses(models.Model):
    
    desc = models.CharField(max_length=200)
    cost = models.IntegerField()
    cashInHand = models.IntegerField()
    date = models.DateField()
    
    def __str__():
        return '%s' % (self.desc)
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
    
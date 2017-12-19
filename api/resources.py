from tastypie.resources import ModelResource
from api.models import *
from tastypie.authorization import Authorization

class allOrders(ModelResource):
    class Meta:
        queryset = order.objects.all()
        resource_name = 'order'
        
class allRawOrders(ModelResource):
    class Meta:
        queryset = rawMaterialOrder.objects.all()
        resource_name = 'rawMat'
        
class allexps(ModelResource):
    class Meta:
        queryset = expenses.objects.all()
        resource_name = 'exps'
        
class pendingOrder(ModelResource):
    class Meta:
        temp = order.objects.filter(delivered = False)
        queryset = temp
        resource_name = 'pendOrder'
        
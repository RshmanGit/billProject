from tastypie.resources import ModelResource
from api.models import *
from tastypie.authorization import Authorization
from datetime import date
from tastypie.validation import Validation
from tastypie.authorization import Authorization

class allOrders(ModelResource):
    class Meta:
        queryset = order.objects.all()
        resource_name = 'order'
        #validation = Validation()
        authorization = Authorization()

class allRawOrders(ModelResource):
    class Meta:
        queryset = rawMaterialOrder.objects.all()
        resource_name = 'rawMat'
        #validation = Validation()
        authorization = Authorization()

class allexps(ModelResource):
    class Meta:
        queryset = expenses.objects.all()
        resource_name = 'exps'
        #validation = Validation()
        authorization = Authorization()

class pendingOrder(ModelResource):
    class Meta:
        temp = order.objects.filter(delivered = False).order_by('order_date')
        queryset = temp
        resource_name = 'pendOrder'

class todayRawMat(ModelResource):
    class Meta:
        temp = rawMaterialOrder.objects.filter(order_date = date.today()).order_by('order_date')
        queryset = temp
        resource_name = 'todayRawMat'

class todayExps(ModelResource):
    class Meta:
        temp = expenses.objects.filter(date = date.today()).order_by('date')
        queryset = temp
        resource_name = 'todayExps'

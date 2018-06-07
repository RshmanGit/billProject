from django.conf.urls import url, include
from django.contrib import admin
from api.resources import allOrders,allRawOrders,allexps,pendingOrder,todayRawMat,todayExps
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(allOrders())
v1_api.register(allRawOrders())
v1_api.register(allexps())
v1_api.register(pendingOrder())
v1_api.register(todayRawMat())
v1_api.register(todayExps())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/', include(v1_api.urls)),
    url(r'^',include('api.urls'))
]
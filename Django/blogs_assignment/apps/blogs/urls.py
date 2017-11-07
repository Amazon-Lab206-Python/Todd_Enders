from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index), # /
    url(r'^new$', views.new), # /new12314234135
    url(r'^(?P<number>\d+\w+)$', views.number), # /123456  /1 /0 /15
]
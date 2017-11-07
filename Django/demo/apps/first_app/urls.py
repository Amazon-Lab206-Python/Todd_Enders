from django.conf.urls import url, include
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^messages$', views.create_message),
    url(r'^comments$', views.create_comment),
    url(r'^logout$', views.logout)
]
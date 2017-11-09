from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^random_word$', views.index),
    url(r'^random_word/generate$', views.generate),
    url(r'^random_word/reset$', views.reset),
]
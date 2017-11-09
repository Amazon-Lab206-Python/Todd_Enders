from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^session_words', views.index),
    url(r'^add_word', views.add),
    url(r'^clear', views.clear),
]

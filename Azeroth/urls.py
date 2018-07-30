from django.conf.urls import url
from django.conf.urls import include
from Azeroth import views


urlpatterns = [
    url(r'^index', views.index),
    url(r'^login', views.login),
]
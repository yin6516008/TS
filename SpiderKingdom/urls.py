from django.conf.urls import url
from django.conf.urls import include
from SpiderKingdom import views


urlpatterns = [
    url(r'^api/domain', views.domain),

]
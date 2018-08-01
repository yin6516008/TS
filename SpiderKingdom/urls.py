from django.conf.urls import url
from django.conf.urls import include
from SpiderKingdom import views

from rest_framework import routers
from SpiderKingdom import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'domains', views.DomainViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'status_codes', views.StatusCodeViewSet)
router.register(r'cdns', views.CDNViewSet)
router.register(r'nodes', views.NodeViewSet)

urlpatterns = [
    # url(r'^api/domain', views.domain),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
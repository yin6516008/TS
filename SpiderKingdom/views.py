
# Create your views here.

from rest_framework import viewsets
from rest_framework import mixins

from django.contrib.auth.models import User, Group
from SpiderKingdom import rest_serializers
from SpiderKingdom import models


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = rest_serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = rest_serializers.GroupSerializer


class DomainViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,viewsets.GenericViewSet):
    """
    List:
        获取域名列表
    Create:
        新建一个域名
    """
    queryset = models.Domain.objects.all()
    serializer_class = rest_serializers.DomainSerializer



class ProjectViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = models.Project.objects.all()
    serializer_class = rest_serializers.ProjectSerializer

class StatusCodeViewSet(viewsets.ModelViewSet):
    queryset = models.StatusCode.objects.all()
    serializer_class = rest_serializers.StatusCodeSerializer

class CDNViewSet(viewsets.ModelViewSet):
    queryset = models.CDN.objects.all()
    serializer_class = rest_serializers.CDNSerializer

class NodeViewSet(viewsets.ModelViewSet):
    queryset = models.Node.objects.all()
    serializer_class = rest_serializers.NodeSerializer

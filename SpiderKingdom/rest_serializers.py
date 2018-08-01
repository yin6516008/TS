from django.contrib.auth.models import User, Group
from SpiderKingdom import models
from SpiderKingdom.models import Domain,Project

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        depth = 2
        fields = '__all__'

class StatusCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StatusCode
        fields = '__all__'

class CDNSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CDN
        fields = '__all__'


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node
        fields = '__all__'
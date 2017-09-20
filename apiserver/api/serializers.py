# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from models import Class, Semester


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


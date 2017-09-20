# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view, list_route
from rest_framework.response import Response
from rest_framework.views import APIView
from serializers import UserSerializer
from models import Class, Semester
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router.register(r'users', UserViewSet)


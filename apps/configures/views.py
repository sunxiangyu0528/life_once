from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from apps.configures.models import Configures
from configures.serializer import ConfiguresModelSerializer


class ConfigViewSet(viewsets.ModelViewSet):
    """
    项目视图
    """
    queryset = Configures.objects.all()
    serializer_class = ConfiguresModelSerializer
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from apps.envs.models import Envs
from apps.envs.serializer import EnvsModelSerializer


class EnvsViewSet(viewsets.ModelViewSet):
    """
    项目视图
    """
    queryset = Envs.objects.all()
    serializer_class = EnvsModelSerializer

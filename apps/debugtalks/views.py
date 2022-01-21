from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from apps.debugtalks.models import DebugTalks
from apps.debugtalks.serializer import DebugModelSerializer


class DebugViewSet(viewsets.ModelViewSet):
    """
    项目视图
    """
    queryset = DebugTalks.objects.all()
    serializer_class = DebugModelSerializer

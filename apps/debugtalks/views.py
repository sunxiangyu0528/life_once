import django_filters
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, mixins, permissions
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.debugtalks.models import DebugTalks
from apps.debugtalks.serializer import DebugModelSerializer
from rest_framework.generics import GenericAPIView

# class DebugViewSet(GenericAPIView):
from utils.pagination import PageNumberPaginationManual


class DebugViewSet(viewsets.ModelViewSet):
    """
    项目视图
    """
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "name", "project"]
    # permission_classes = [permissions.IsAdminUser]
    queryset = DebugTalks.objects.all()
    serializer_class = DebugModelSerializer

    # 分页
    pagination_class = PageNumberPaginationManual

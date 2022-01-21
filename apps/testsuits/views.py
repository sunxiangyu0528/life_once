from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from apps.testsuits.models import TestSuites
from apps.testsuits.serializer import SuitSerializer


class SuitViewSet(viewsets.ModelViewSet):
    """
    项目视图
    """
    queryset = TestSuites.objects.all()
    serializer_class = SuitSerializer

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from apps.testcases.serializer import TestCasesSerializer
from apps.testcases.models import TestCases


class CaseViewSet(viewsets.ModelViewSet):
    """
    项目视图
    """
    queryset = TestCases.objects.all()
    serializer_class = TestCasesSerializer

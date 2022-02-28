from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView

from apps.reports.models import Reports
from apps.reports.serializer import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    """
    项目视图
    """
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer

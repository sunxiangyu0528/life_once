import json

from django.http import JsonResponse, Http404
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import Projects
from projects.serializer import ProjectModelSerializer
from utils.pagination import PageNumberPaginationManual


class ProjectsList(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    pagination_class = PageNumberPaginationManual

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_fields = ['name', 'leader']

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

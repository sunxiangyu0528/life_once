import json

from django.http import JsonResponse, Http404
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import Projects
from projects.serializer import ProjectModelSerializer
from utils.pagination import PageNumberPaginationManual


class ProjectsList(GenericAPIView):
    queryset = Projects.objects.all().order_by("id")
    serializer_class = ProjectModelSerializer

    # 排序
    # filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'leader']

    # 过滤
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name', 'leader']
    pagination_class = PageNumberPaginationManual

    def get(self, request):
        # project = Projects.objects.all()
        # serializer = ProjectModelSerializer(instance=project, many=True)
        project_qs = self.get_queryset()
        project_qs = self.filter_queryset(project_qs)
        page = self.paginate_queryset(project_qs)
        if page is not None:
            serializer = self.get_serializer(instance=page, many=True)
            self.get_paginated_response(serializer.data)

        return Response(serializer.data, status=201)

    def post(self, request):
        json_data = request.body.decode('utf-8')
        py_data = json.loads(json_data, encoding='utf-8')
        serializer = ProjectModelSerializer(data=py_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)
        serializer.save()
        # project = Projects.objects.create(**serializer.validated_data)
        return JsonResponse(serializer.data, status=201)


class ProjectsDetail(GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['name', 'leader']
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'leader']

    # lookup_field = 'id'
    def get(self, request, pk):
        project = self.get_object()
        serializer = self.get_serializer(instance=project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object()

        json_data = request.body.decode('utf-8')
        py_data = json.loads(json_data, encoding='utf-8')
        serializer = self.get_serializer(instance=project, data=py_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)
        serializer.save()
        # project = Projects.objects.create(**serializer.validated_data)

        return JsonResponse(serializer.data, status=201)

    def delete(self, request, pk):
        project = self.get_object()
        project.delete()
        return Response(None, status=204)

    def post(self, request):
        data = request.body.decode('utf-8')
        py_date = json.loads(data)
        serializer = ProjectModelSerializer(data=py_date)
        try:
            serializer.is_valid()
        except Exception as e:
            return serializer.errors
        project = Projects.objects.create(**serializer.validated_data)
        return JsonResponse(serializer.data, status=201)

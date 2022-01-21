from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.interfaces.models import Interface
from apps.interfaces.serializer import InterfaceModelSerializer


class InterfaceViewSet(viewsets.ModelViewSet):
    """
    项目视图
    """
    queryset = Interface.objects.all()
    serializer_class = InterfaceModelSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='id11', url_name='url_names')
    def id_1(self, request):
        project = Interface.objects.filter(project_id=2)
        serializer = InterfaceModelSerializer(instance=project,many=True)
        # return Response(serializer.data)
        return Response(serializer.data)
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status

from apps.projects.models import Projects
from apps.projects.serializer import ProjectModelSerializer, \
    ProjectNameSerializer, InterfaceByProjectIdSerializer
from rest_framework import generics
# ViewSet不再支持get，post，put等请求方法，只支持action动作
from apps.projects.utils import get_count_by_project, get_create_date
from utils.pagination import PageNumberPaginationManual


class ProjectsViewSet(viewsets.ModelViewSet):
    """
    项目视图
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    ordering_fields = ['id', 'name']
    filterset_fields = ['id', 'name']
    pagination_class = PageNumberPaginationManual

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    @action(methods=['GET'], detail=False, url_path='nm', url_name='url_names')
    def names(self, request):
        project = self.get_queryset()
        serializer = ProjectNameSerializer(instance=project, many=True)
        # return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    # 获取项目id为1的所有接口
    @action(detail=True)
    def interfaces(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = InterfaceByProjectIdSerializer(instance=instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas = serializer.data
            datas = get_count_by_project(datas)
            return self.get_paginated_response(datas)

        serializer = self.get_serializer(queryset, many=True)
        datas = serializer.data
        datas = get_count_by_project(datas)
        return Response(datas)

    def create(self, request, *args, **kwargs):
        data=get_create_date(request)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve()

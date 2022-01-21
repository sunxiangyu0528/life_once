import json

from django.http import JsonResponse, Http404
from django.views import View

from projects.models import Projects
from projects.serializer import ProjectSerializer


class ProjectsList(View):
    def get(self, request):
        project = Projects.objects.all()
        serializer = ProjectSerializer(instance=project, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        json_data = request.body.decode('utf-8')
        py_data = json.loads(json_data, encoding='utf-8')
        serializer = ProjectSerializer(data=py_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)
        serializer.save()
        # project = Projects.objects.create(**serializer.validated_data)
        return JsonResponse(serializer.data, status=201)


class ProjectsDetail(View):
    def get_object(self, pk):
        try:
            return Projects.objects.get(id=pk)

        except Projects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(instance=project)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        json_data = request.body.decode('utf-8')
        py_data = json.loads(json_data, encoding='utf-8')
        serializer = ProjectSerializer(instance=project, data=py_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)
        serializer.save()
        # project = Projects.objects.create(**serializer.validated_data)

        return JsonResponse(serializer.data, status=201)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return

    def post(self, request):
        data = request.body.decode('utf-8')
        py_date = json.loads(data)
        serializer = ProjectSerializer(data=py_date)
        try:
            serializer.is_valid()
        except Exception as e:
            return serializer.errors
        project = Projects.objects.create(**serializer.validated_data)
        return JsonResponse(serializer.data, status=201)

import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from projects.models import Projects


def index(request):
    print(request.method)

    return JsonResponse({'hello': 'world'})


class IndexView(View):
    def get(self, request):
        # 第一种方法创建
        # one_obj = Projects(name='q21', leader='sss', programer='sss', publish_app='sss', desc='sfds')
        # one_obj.save()
        # 第二种方法创建
        # Projects.objects.create(name='q22', leader='sss', programer='sss', publish_app='sss', desc='sfds')
        # one = Projects.objects.filter(id=1)
        # qs = Projects.objects.filter(interfaces__name='这是一个接口项目')
        # 外键字段__从表的字段名
        one = Projects.objects.filter(interface__name='这是一个接口项目')

        # Projects.objects.filter()

        return JsonResponse({'hello': 'world'})

    def post(self, request):
        one_str = request.body.decode('utf-8')
        one_dict = json.loads(one_str)
        print(one_dict['name'])
        return JsonResponse({'hello': 'world'})

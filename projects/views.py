import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def index(request):
    print(request.method)

    return JsonResponse({'hello': 'world'})


class IndexView(View):
    def get(self, request, pk):
        print(request.method)
        # print(request.GET['name'])
        return JsonResponse({'hello': 'world'})

    def post(self, request):
        one_str = request.body.decode('utf-8')
        one_dict = json.loads(one_str)
        print(one_dict['name'])
        return JsonResponse({'hello': 'world'})

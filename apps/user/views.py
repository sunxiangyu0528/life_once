# from django.shortcuts import render
#
# # Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.user.serializer import RegisterSerializer


class RegisterView(CreateAPIView):
    # queryset =
    serializer_class = RegisterSerializer
    # authwn = (JSONWebTokenAuthentication,)
    authentication_classes = (JSONWebTokenAuthentication,)
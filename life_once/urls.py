"""learndjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="lemon_ban",
        default_version='v1',
        description="这是一个美轮美奂的接口文档",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="1340518678@qq.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [path('admin/', admin.site.urls),
               path('', include('apps.projects.urls')),
               path('', include('apps.configures.urls')),
               path('', include('apps.interfaces.urls')),
               path('', include('apps.envs.urls')),
               path('', include('apps.debugtalks.urls')),
               path('', include('apps.reports.urls')),
               path('', include('apps.testsuits.urls')),
               path('', include('apps.testcases.urls')),
               path('user/', include('apps.user.urls')),
               path('dos/', include_docs_urls(title="测试平台接口文档", description='这是一个美轮美奂的接口文档平台')),
               re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                       name='schema-json'),
               re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
               re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
               path('api/', include('rest_framework.urls')),
               path('user/', include('apps.user.urls'))
               ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('projects.urls')),
#     path('dos/', include_docs_urls(title="测试平台接口文档",
#                                    description='这是一个美轮美奂的接口文档平台'))
#
# ]

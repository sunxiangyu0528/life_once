from django.conf.urls import url
from django.urls import path
from apps.debugtalks import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

#  创建SimpleRouter路由对象
router = routers.SimpleRouter()
# 注册路由，第一个参数为路由前缀，一般添加应用名即可
# 第二个参数ViewSet为视图集，不要加as.view()
router.register(r'debug', views.DebugViewSet)

urlpatterns = [

    path('debug_test', obtain_jwt_token),
]

urlpatterns += router.urls

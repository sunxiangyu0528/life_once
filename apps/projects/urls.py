from apps.projects import views
from rest_framework import routers

#  创建SimpleRouter路由对象
router = routers.SimpleRouter()
# 注册路由，第一个参数为路由前缀，一般添加应用名即可
# 第二个参数ViewSet为视图集，不要加as.view()
router.register(r'project', views.ProjectsViewSet)

urlpatterns = [
    # path('project/', views.ProjectsViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # }), name='project_list'),
    # path('project/<int:pk>/', views.ProjectsViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # }), name="project_detail"),
    # path('project/names/', views.ProjectsViewSet.as_view({
    #     'get': 'names'
    # }), name='project_names'),
    # path('project/<int:pk>/interfaces/', views.ProjectsViewSet.as_view({
    #     'get': 'interfaces'
    # }), name='project_names'),
]

urlpatterns += router.urls

from django.urls import path

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

router = routers.SimpleRouter()
from user import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', views.RegisterView.as_view()),

]

urlpatterns += router.urls

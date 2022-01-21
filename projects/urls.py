from django.contrib import admin
from django.urls import path, include

from projects import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('projects/', views.ProjectsList.as_view()),
    path('projects/<int:pk>/', views.ProjectsDetail.as_view())
]

from django.contrib import admin
from django.urls import path, include

from projects import views
from projects.views import index, IndexView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.IndexView.as_view()),
    path('index/<int:pk>/', views.IndexView.as_view())
]

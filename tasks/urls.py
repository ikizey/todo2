from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("todos.urls")),
    path('admin/', admin.site.urls),
]

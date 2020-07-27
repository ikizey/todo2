from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name="hello"),
    path('todos/<str:user_name>/', views.todo, name="todo"),
]

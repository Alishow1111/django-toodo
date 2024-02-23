from django.urls import path
from . import views

urlpatterns = [
    path('api', views.TodoListApiView.as_view()),
    path('api/<int:todo_id>', views.TodoDetailApiView.as_view()),
]
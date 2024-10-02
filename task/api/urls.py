from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('task/<int:id>', views.api_task_detail, name='task-detail'),
]
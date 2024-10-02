from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('task/<int:id>', views.api_task_detail, name='task-detail'),
    path('task/<int:pk>/update', views.api_task_update, name="task-update"),
    path('task/<int:pk>/delete', views.api_task_delete, name="task-delete"),
    path('task/create', views.api_task_create, name='task-create')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_task, name="show_task"),
    path('task/<int:pk>', views.TaskDetail.as_view(), name="task_detail"),
    path('<int:id>/delete', views.delete_task, name="delete_task"),
]

from django.urls import path

from tasks.apps import TasksConfig
from tasks.views import TaskCreateAPIView, TaskListAPIView, TaskRetrieveAPIView, TaskUpdateAPIView, \
    TaskDestroyAPIView

app_name = TasksConfig.name

urlpatterns = [
    path('task/create/', TaskCreateAPIView.as_view(), name='task_create'),
    path('task/', TaskListAPIView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskRetrieveAPIView.as_view(), name='task_get'),
    path('task/update/<int:pk>/', TaskUpdateAPIView.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDestroyAPIView.as_view(), name='task_delete'),
]

from django.urls import path
from .views import create_task, assign_task, task_list, user_tasks

urlpatterns = [
    path('create/', create_task, name='create_task'),
    path('assign/', assign_task, name='assign_task'),
    path('', task_list, name='task_list'),
    path('user/<int:user_id>/', user_tasks, name='user_tasks'),
]

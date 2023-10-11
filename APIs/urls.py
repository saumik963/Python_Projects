from django.urls import path
from .views import TaskListCreateView, TaskCRUDView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskCRUDView.as_view(), name='task-retrieve-update-destroy'),
]

from django.urls import path
from . import views

urlpatterns = [

    path('', views.TasksView.as_view(), name='show'),
    path('complete_tasks/', views.Complete.as_view(), name='complete_tasks'),
    path('form/', views.Input.as_view(), name='form'),
    path('edit/<int:pk>', views.TasksUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', views.DeleteTask.as_view(), name='delete'),
    path('is_complete/<int:id>/', views.TaskComplete, name='complete'),

]

from django.urls import path
from . import views
urlpatterns=[

    path('', views.TaskView.as_view(), name='home'),
    path('comlete/tasks/',views.CompleteTasksView.as_view(),name='completed'),


    # CRUD operations
    path('task/complete/<int:id>/', views.TaskCompleteView.as_view(), name='task_complete'),
    path('Delete/<int:pk>', views.DeleteTask.as_view(), name='Delete'),
    path('Update/<int:pk>', views.TasksUpdate.as_view(), name='Update'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='detail'),

    # Account urls
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/',views.UserLoginView.as_view(), name='login'),
    path('logout/',views.logout.as_view(), name='logout'),
    path('password/update/', views.PasswordUpdateView.as_view(), name='password_update'),


]
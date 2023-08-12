from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'taskTitle', 'taskDescription', 'is_completed']

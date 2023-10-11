from django.contrib import admin
from . import models
# Register your models here.

class TaskImageAdmin(admin.StackedInline):
    model=models.TaskImages


@admin.register(models.Tasks)
class TaskAdmin(admin.ModelAdmin):
    inlines=[TaskImageAdmin]
    list_display = ['user', 'taskTitle', 'taskDescription',"Priority" ,'is_completed']


@admin.register(models.TaskImages)

class TaskImageAdmin(admin.ModelAdmin):
    pass

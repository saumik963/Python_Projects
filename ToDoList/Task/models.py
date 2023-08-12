from django.db import models

# Create your models here.


class ToDoList(models.Model):
    id = models.IntegerField(primary_key=True)
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.CharField(max_length=500)
    is_completed = models.BooleanField(default=False)

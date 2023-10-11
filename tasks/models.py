from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tasks(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.CharField(max_length=1000)
    Priority = models.IntegerField(choices=PRIORITY_CHOICES)
    # images=models.ImageField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.taskTitle
    
class TaskImages(models.Model):
    task=models.ForeignKey(Tasks,default=None,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='TaskImage')

    def __str__(self) :
        return self.task.taskTitle


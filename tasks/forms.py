from django import forms
from .models import Tasks,TaskImages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class TasksForm(forms.ModelForm):
#     class Meta:
#         model = Tasks
#         fields = ['taskTitle', 'taskDescription', 'Priority']
#         widgets = {
#             'Priority': forms.Select(choices=Tasks.PRIORITY_CHOICES),
#         }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ChangeUserData(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['taskTitle', 'taskDescription', 'Priority']

class TaskImagesForm(forms.ModelForm):
    class Meta:
        model = TaskImages
        fields = ['image']
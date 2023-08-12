from django import forms
from Task.models import ToDoList


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['taskTitle', 'taskDescription']

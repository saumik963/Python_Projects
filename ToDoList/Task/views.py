from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from Task.models import ToDoList
from Task.forms import ToDoForm
from django.urls import reverse_lazy

# Create your views here.


class Complete(ListView):
    model = ToDoList
    template_name = "complete_tasks.html"
    context_object_name = 'data'


class Input(CreateView):
    model = ToDoList
    form_class = ToDoForm
    template_name = 'edit_form.html'
    success_url = reverse_lazy('show')


def TaskComplete(request, id):
    task = ToDoList.objects.get(id=id)
    task.is_completed = True
    task.save()
    return redirect('complete_tasks')


class TasksView(ListView):
    model = ToDoList
    template_name = 'show_tasks.html'
    context_object_name = 'data'


class TasksUpdate(UpdateView):
    model = ToDoList
    template_name = 'edit_form.html'
    form_class = ToDoForm
    success_url = reverse_lazy('show')


class DeleteTask(DeleteView):
    model = ToDoList
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('show')

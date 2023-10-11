from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import UpdateView, DeleteView,DetailView
from .models import Tasks,TaskImages
from .forms import TasksForm,TaskImagesForm
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login,update_session_auth_hash
from django.core.paginator import Paginator
from django.views import View
from django.contrib.auth.views import LogoutView


# Create your views here.

# Add and view tasks
class TaskView(View):
    template_name = 'tasks_list.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login")

        tsk = request.GET.get('searchtask')
        if tsk:
            tasks = Tasks.objects.filter(taskTitle__icontains=tsk, user=request.user)
        else:
            tasks = Tasks.objects.filter(user=request.user)

        sorting_option = request.GET.get('sorting_option')
        if sorting_option == '1':
            tasks = tasks.order_by('Priority')
        elif sorting_option == '3':
            tasks = tasks.order_by('-Priority')

        paginator = Paginator(tasks, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        task_count=tasks.count()

        context = {
            'tasks': page_obj,
            'home_act': 'active',
            'task_count':task_count,
            'form': TasksForm(),
        }

        return render(request, self.template_name, context)

    def post(self, request):
        task_form = TasksForm(request.POST, request.FILES)
        image_form = TaskImagesForm(request.POST, request.FILES)
        
        if task_form.is_valid() and image_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            task.save()

            images = request.FILES.getlist('image')  # Get list of uploaded images
            for image in images:
                TaskImages.objects.create(task=task, image=image)  # Associate each image with the task

            messages.success(request, 'Task and images added successfully.')
            return redirect('home')  # Redirect to a success page
        else:
            tasks = Tasks.objects.filter(user=request.user)
            paginator = Paginator(tasks, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                'tasks': page_obj,
                'home_act': 'active',
                'form': task_form,
                'image_form': image_form,
            }
            
            return render(request, self.template_name, context)


# Show completed tasks

class CompleteTasksView(View):
    template_name = 'completes.html'

    def get(self, request):
        tasks = Tasks.objects.filter(user=request.user, is_completed=True)

        sorting_option = request.GET.get('sorting_option')
        if sorting_option == '1':
            tasks = tasks.order_by('Priority')
        elif sorting_option == '3':
            tasks = tasks.order_by('-Priority')

        context = {
            'tasks': tasks,
            'com_act': 'active',
        }
        return render(request, self.template_name, context)

# Detail view of the task

class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'task_detail.html'  
    context_object_name = 'task'  


# Delete the task

class DeleteTask(DeleteView):
    model = Tasks
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('home')

# Edit and update the task

class TasksUpdate(UpdateView):
    model = Tasks
    template_name = 'task_update.html'
    form_class = TasksForm
    success_url = reverse_lazy('home')


# Button for complete or incomplete

class TaskCompleteView(View):
    def get(self, request, id):
        task = get_object_or_404(Tasks, id=id)
        if task.is_completed == False:
            task.is_completed = True
        else:
            task.is_completed = False
        task.save()
        return redirect('home')



# User authentications

class SignupView(View):
    template_name = 'signup.html'

    def get(self, request):
        if not request.user.is_authenticated:
            form = RegisterForm()
            return render(request, self.template_name, {'form': form, "sup_act": "active"})
        else:
            return redirect("home")

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
            return redirect("login")
        return render(request, self.template_name, {'form': form, "sup_act": "active"})
    

class UserLoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if not request.user.is_authenticated:
            form = AuthenticationForm()
            return render(request, self.template_name, {'form': form, "sin_act": "active"})
        else:
            return redirect("home")

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=name, password=userpass)

            if user is not None:
                login(request, user)
                return redirect('home')
        
        return render(request, self.template_name, {'form': form, "sin_act": "active"})
    

class logout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return redirect('login')  
    

class PasswordUpdateView(View):
    template_name = 'pass_update.html'

    def get(self, request):
        if request.user.is_authenticated:
            form = PasswordChangeForm(user=request.user)
            return render(request, self.template_name, {'form': form,'pas_act':'active'})
        else:
            return redirect('login')

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})
    

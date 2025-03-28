from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskForm, TaskAssignForm

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def assign_task(request):
    if request.method == "POST":
        form = TaskAssignForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            users = form.cleaned_data['users']
            task.assigned_users.set(users)
            return redirect('task_list')
    else:
        form = TaskAssignForm()
    return render(request, 'tasks/assign_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def user_tasks(request, user_id):
    user = get_object_or_404(User, id=user_id)
    tasks = user.tasks.all()
    return render(request, 'tasks/user_tasks.html', {'tasks': tasks, 'user': user})

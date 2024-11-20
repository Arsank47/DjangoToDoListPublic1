# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

@login_required
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}! You can now log in.")
            return redirect('login')  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Only show tasks related to the logged-in user
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = Task.objects.create(title=title, description=description, user=request.user)  # Associate task with logged-in user
        return redirect('task_list')
    return render(request, 'tasks/task_create.html')

@login_required
def task_update(request, pk):
    task = Task.objects.get(id=pk, user=request.user)  # Ensure task belongs to logged-in user
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_update.html', {'task': task})

@login_required
def task_delete(request, pk):
    task = Task.objects.get(id=pk, user=request.user)  # Ensure task belongs to logged-in user
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_delete.html', {'task': task})

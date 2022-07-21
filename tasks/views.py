from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.


def view_tasks(request):
    context = {
        'pending_tasks': Task.objects.filter(is_done=False)
    }
    return render(request, 'dashboard.html', context)


def create_task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'create_task.html', context)


def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'create_task.html', context)

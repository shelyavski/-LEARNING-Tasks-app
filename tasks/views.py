from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def view_tasks(request):
    context = {
        'tasks': Task.objects.filter(is_done=False),
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def view_completed_tasks(request):
    context = {
        'tasks': Task.objects.filter(is_done=True),
    }
    return render(request, 'completed_tasks.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
@require_POST
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

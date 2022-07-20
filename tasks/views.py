from django.shortcuts import render
from .models import Task

# Create your views here.


def view_tasks(request):
    context = {
        'all_tasks': Task.objects.all()
    }
    return render(request, 'dashboard.html', context)

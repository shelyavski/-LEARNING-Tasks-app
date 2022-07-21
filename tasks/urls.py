from django.urls import path
from .views import *

urlpatterns = [
    path('', view_tasks, name='dashboard'),
    path('create_task/', create_task, name='create_task'),
    path('update_task/<str:pk>', edit_task, name='edit_task'),
]

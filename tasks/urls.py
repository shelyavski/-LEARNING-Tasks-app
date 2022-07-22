from django.urls import path
from .views import *

urlpatterns = [
    path('', view_tasks, name='dashboard'),
    path('create_task/', create_task, name='create_task'),
    path('update_task/<str:pk>', edit_task, name='edit_task'),
    path('delete_task/<str:pk>', delete_task, name='delete_task'),
    path('completed/', view_completed_tasks, name='completed_tasks'),
]

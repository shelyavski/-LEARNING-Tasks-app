from django.contrib import admin
from django.db import models
from users.models import Profile

# Create your models here.


class Task(models.Model):
    TASK_PRIORITIES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    )

    title = models.CharField(max_length=70,)
    date_created = models.DateField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    priority = models.CharField(max_length=6, choices=TASK_PRIORITIES)
    owner = models.ForeignKey(Profile, blank=True, null=True, editable=False, on_delete=models.CASCADE, related_name='owner')
    assigned_members = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.RESTRICT, related_name='assigned_members')

    def __str__(self):
        return self.title


class TaskAdmin(admin.ModelAdmin):  # Displays custom fields in Admin page.
    list_display = ('title', 'date_created', 'is_done', 'priority', 'owner', 'assigned_members')

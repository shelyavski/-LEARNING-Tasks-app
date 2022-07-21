from django.contrib import admin
from django.db import models

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

    def __str__(self):
        return self.title


class TaskAdmin(admin.ModelAdmin):  # Displays custom fields in Admin page.
    list_display = ('title', 'priority', 'date_created')

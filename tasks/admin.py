from django.contrib import admin
from tasks.models import Task, TaskAdmin
# Register your models here.


admin.site.register(Task, TaskAdmin)

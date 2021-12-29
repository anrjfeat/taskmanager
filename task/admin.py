from django.contrib import admin
from task.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','email','createdAt']


# Register your models here.

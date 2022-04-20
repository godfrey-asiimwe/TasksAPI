from django.contrib import admin

# Register your models here.
from .models import Task


class task(admin.ModelAdmin):
    list_display = (
       'task_id','name', 'description','status')
    search_fields = ['name']


admin.site.register(Task, task)
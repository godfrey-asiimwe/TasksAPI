from django.db.models import fields
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','task_id','name', 'description','status', 'start_date', 'end_date','responsible','projectId','created_by','created_on')

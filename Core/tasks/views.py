from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serlializers import TaskSerializer
from rest_framework import serializers
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_projects': '/all',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete',
        'View': '/view/pk'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_tasks(request):
    task = TaskSerializer(data=request.data)

    # validating for already existing data
    if Task.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if task.is_valid():

        task.save()
        return Response(task.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_tasks(request):
    # checking for the parameters from the URL
    tasks = Task.objects.all()

    if tasks:
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_tasksByID(request, pk):
    # checking for the parameters from the URL
    task = Task.objects.get(pk=pk)

    if task:
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_Tasks(request, pk):
    task = Task.objects.get(pk=pk)
    data = TaskSerializer(instance=task, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

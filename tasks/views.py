from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import permissions, status
from . import models
from .serializers import TaskSerializer
from rest_framework.response import Response

# Create your views here.

class TaskView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tasks = models.Task.objects.filter(user=request.user).order_by('id')
        serialized_tasks = TaskSerializer(tasks, many=True)
        return Response({'tasks': serialized_tasks.data, 'username': request.user.username})

    def post(self, request):
        datadict = request.data.copy()
        datadict['user'] = request.user.id
        serialized_task = TaskSerializer(data=datadict)
        if serialized_task.is_valid():
            serialized_task.save()
            return Response(serialized_task.data)
        return Response(status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request):
        datadict = request.data.copy()
        datadict['user'] = request.user.id
        try:
            task_inst = models.Task.objects.get(pk=datadict['id'])
        except:
            task_inst = None
        if task_inst != None:
            serilazied_task = TaskSerializer(task_inst, data=datadict)
            if serilazied_task.is_valid():
                serilazied_task.save()
                return Response(serilazied_task.data)
        return Response({'error': 'no such task'})

    def delete(self, request):
        try:
            task_inst = models.Task.objects.get(pk=request.data['id'])
        except:
            task_inst = None
        if task_inst != None:
            task_inst.delete()
            return Response({'message': 'successfully deleted'})
        return Response({'error': 'no such task'})


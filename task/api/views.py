from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import TodoTask
from .serializers import TodoTaskSerializer


@api_view(['GET'])
def task_list(request):
    if request.method == "GET":
        query = TodoTask.objects.all()
        serializer = TodoTaskSerializer(query, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def api_task_detail(request, id):
    try:
        task = TodoTask.objects.get(pk=id)
    except TodoTask.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = TodoTaskSerializer(task)
        return Response(serializer.data)


@api_view(['PUT'])
def api_task_update(request, pk):
    try:
        task = TodoTask.objects.get(pk=pk)
    except TodoTask.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {}
    if request.method == 'PUT':
        serializer = TodoTaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['anjam shod'] = "update anjam shod"
            return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_task_delete(request, pk):
    try:
        task = TodoTask.objects.get(pk=pk)
    except TodoTask.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {}
    if request.method == "DELETE":
        task.delete()
        data['hazf shod'] = "hazf anjam shod"
        return Response(data=data)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def api_task_create(request):
    data = {}
    if request.method == "POST":
        serializer = TodoTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['anjam shod'] = "task jadidi sakhte shod"
            return Response(data=data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from task.serializers import TaskSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from task.models import Task


@csrf_exempt
def task_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=TaskSerializer(data=pythondata)

        if serializer.is_valid():
            serializer.save()
            result = {'message':'Data Created'}
            json_data = JSONRenderer().render(result)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

def task_all(request):
    taskall=Task.objects.all()
    serializer=TaskSerializer(taskall, many=True)
    data={"data":serializer.data}
    return JsonResponse(data,safe=False)



from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Upload
from api.serializers import UploadSerializer


@csrf_exempt
def upload_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        upload = Upload.objects.all()
        serializer = UploadSerializer(upload, many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UploadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
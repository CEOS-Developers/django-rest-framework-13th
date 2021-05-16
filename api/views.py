from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Profile, Upload
from api.serializers import ProfileSerializer, UploadSerializer, UploadListSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class IsAuthorPostorUpdate(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        if request.method != 'GET':
            return obj.profile == request.user


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class UploadFilter(FilterSet):
    description = filters.CharFilter(field_name="description", lookup_expr="icontains")
    is_profile = filters.BooleanFilter(method='filter_is_profile')
    profile = filters.NumberFilter(field_name="profile")

    class Meta:
        model = Upload
        fields = ['id', 'description', 'profile']

    def filter_is_profile(self, queryset, name, value):
        filtered_queryset = queryset.filter(profile=2)
        return filtered_queryset


class UploadViewSet(viewsets.ModelViewSet):
    serializer_class = UploadSerializer
    queryset = Upload.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UploadFilter
    permission_classes = (IsAuthorPostorUpdate,)


''' FBV 방식
@csrf_exempt # 해킹 방지?
def upload_list(request):
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
'''
'''
#image 파일 보완필요, 기능 정리 필요

class UserList(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True) # Queryset일 경우 many=True
        return JsonResponse(serializer.data, safe=False) # python data type이 dict가 아닐 경우 safe=False
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class UserUpload(APIView):
    def get(self, request, pk, format=None):
        profile = Profile.objects.get(id=pk)
        upload = Upload.objects.filter(profile=profile)
        serializer = UploadListSerializer(upload, many=True)
        return JsonResponse(serializer.data, safe=False)
    def post(self, request, pk, format=None):
        data = JSONParser().parse(request)
        serializer = UploadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class UploadList(APIView):
    def get(self, request, format=None):
        upload = Upload.objects.all()
        serializer = UploadListSerializer(upload, many=True)
        return JsonResponse(serializer.data, safe=False)

class UploadFix(APIView):
    def put(self, request, pk, format=None):
        data = JSONParser().parse(request)
        upload = Upload.objects.get(id=pk)
        serializer = UploadSerializer(upload, data=data) # 수정 방식
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    def delete(self, request, pk, format=None):
        upload = Upload.objects.get(id=pk)
        upload.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileList(APIView):
    def get(self, request, format=None):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FollowList(APIView):
    def get(self, request, format=None):
        follows = Follow.objects.all()
        serializer = FollowSerializer(follows, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Follow 해당되는 것만 가져온다
class FollowListOne(APIView):
    def get(self, request, pk, format=None):#불러오기
        follows = get_object_or_404(Follow, pk=pk)
        serializer = FollowSerializer(follows)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):#삭제
        follows = get_object_or_404(Follow, pk=pk)
        follows.delete()
        return Response("delete ok", status=status.HTTP_204_OK) #상태코드 delete에 맞게

    def put(self, request, pk, format=None):#업데이트
        follows = get_object_or_404(Follow, pk=pk)
        serializer = FollowSerializer(follows, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HeartList(APIView):
    def get(self, request, format=None):
        hearts = Heart.objects.all()
        serializer = HeartSerializer(hearts, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = HeartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
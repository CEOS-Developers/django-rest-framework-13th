from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import User, Profile, Post
from .serializers import UserSerializer, PostSerializer, ProfileSerializer
from .filters import PostFilter, ProfileFilter, UserFilter


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProfileFilter


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

'''
class PostList(APIView):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response("post does not exist", status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post)  # 하나의 객체만 serialize 하므로 many=True 삭제
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response("post does not exist", status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response("post does not exist", status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response("Post Deleted", status=status.HTTP_204_NO_CONTENT)
'''

'''
class UserList(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response("user does not exist", status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)  # many=True 삭제이유
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response("user does not exist", status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response("user does not exist", status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response("User Deleted", status=status.HTTP_204_NO_CONTENT)
'''
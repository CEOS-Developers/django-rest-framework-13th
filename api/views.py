from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

class UserFilter(FilterSet):
    nickname = filters.CharFilter(field_name='nickname', lookup_expr="icontains")
    is_hy1 = filters.BooleanFilter(method='filter_is_hy1')

    class Meta:
        model = User
        fields = ['nickname']

    def filter_is_hy1(self, queryset, name, value):
        filtered_queryset = queryset.filter(nickname__contains="1")
        filtered_queryset2 = queryset.filter(~Q(nickname__contains="1"))
        if value == True:
            return filtered_queryset
        else:
            return filtered_queryset2
        
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

class PostViewSet(viewsets.ModelViewSet):
	serializer_class = PostSerializer
	queryset = Post.objects.all()

class FileViewSet(viewsets.ModelViewSet):
	serializer_class = FileSerializer
	queryset = File.objects.all()

class FollowViewSet(viewsets.ModelViewSet):
	serializer_class = FollowSerializer
	queryset = Follow.objects.all()

class HeartViewSet(viewsets.ModelViewSet):
	serializer_class = HeartSerializer
	queryset = Heart.objects.all()
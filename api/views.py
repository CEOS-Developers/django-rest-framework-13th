from rest_framework import status, mixins

from .models import Post
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.http import HttpResponse
from django.views import View
# FBV
from rest_framework.decorators import api_view
from rest_framework.response import Response
# CBV
from .serializers import PostSerializer
from rest_framework.views import APIView
# ViewSet
from rest_framework import viewsets
# Filter
from django_filters.rest_framework import FilterSet, filters, DjangoFilterBackend


#
# @csrf_exempt
# def post_list(request):
#     """
#     List all code posts, or create a new post.
#     """
#     # view data
#     if request.method == 'GET':
#         post = Post.objects.all()  # get queryset of the Post
#         serializer = PostSerializer(post, many=True)  # Serialize it to python native data type
#         return JsonResponse(serializer.data, safe=False)  # response with JSON
#
#     # add data
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)  # parse the JSON data
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()  # save to DB
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

#
# #pk가 없는 애
# class PostList(APIView):
#     # 작성한 포스트를 모든 데이터를 가져오는 API 만들기
#     def get(self, request):
#         post = Post.objects.all()  # get queryset of the Post
#         serializer = PostSerializer(post, many=True)  # Serialize it to python native data type
#         return Response(serializer.data)
#
#
#     #새로운 포스트를 create하는 api
#     def post(self, request):
#         data = request.data
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()  # save to DB
#             return Response(serializer.data)
#         return Response(serializer.errors)

# #pk가 있는 애들
# class PostDetail(APIView):
#     # pk가 있는지 없는지 검사
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404
#
#     # 특정 포스트를 들고오는 API
#     def get(self, request, pk):
#         post = self.get_object(pk=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     # 특정 포스트를 update하는 api
#     def put(self, request, pk):
#         post = self.get_object(pk=pk)
#         data = request.data
#         serializer = PostSerializer(post, data)
#         if serializer.is_valid():
#             serializer.save()  # save to DB
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#     # 특정 포스트를 삭제하는 api
#     def delete(self, request, pk):
#         post = self.get_object(pk=pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Filter


class authorFilter(FilterSet):
    author_value = filters.CharFilter(method='filter_author')
    is_good_value = filters.BooleanFilter(method='filter_is_good')

    class Meta:
        model = Post
        fields = '__all__'

    def filter_author(self, queryset, value, *args):
        return queryset.filter(author=args[0])

    def filter_is_good(self, queryset, value):
        if value == True:
            return queryset.filter(is_good=True)
        else :
            return queryset.filter(is_good=False)


# ViewSet으로 class
class PostViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = authorFilter

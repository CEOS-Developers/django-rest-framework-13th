from django.urls import path
from .views import UserViewSet, PostViewSet

user_list = UserViewSet.as_view({
    'get': 'list',
    'put': 'create'
})

post_list = PostViewSet.as_view({
    'get': 'list',
    'put': 'create'
})

urlpatterns = [
    path('api/users', user_list, name='user-list'),
    path('api/posts', post_list, name='post-list')
]

from django.urls import path
from .views import UserViewSet, PostViewSet

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('api/users', user_list, name='user-list'),
    path('api/posts', post_list, name='post-list')
]

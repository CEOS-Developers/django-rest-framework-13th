from django.urls import path
from .views import UserList, PostList

urlpatterns = [
    path('api/users', UserList.as_view()),
    path('api/posts', PostList.as_view())
]

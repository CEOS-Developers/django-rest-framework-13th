from django.urls import path
from api import views

urlpatterns = [
    path('users', views.UserList.as_view()),
    path('posts', views.PostList.as_view()),
    path('files', views.FileList.as_view()),
    path('follows', views.FollowList.as_view()),
    path('hearts', views.HeartList.as_view()),
]
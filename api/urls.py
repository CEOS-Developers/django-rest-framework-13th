from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListAll.as_view()),
    path('posts/<int:pk>/', views.PostList.as_view()),
    path('users/', views.UserListAll.as_view()),
    path('users/<int:pk>/', views.UserList.as_view()),
]
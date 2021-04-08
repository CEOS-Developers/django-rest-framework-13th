from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListAll.as_view()),
    path('posts/<int:pk>/', views.PostList.as_view()),
    path('profiles/', views.profilesList),
    path('users/', views.usersList),
]
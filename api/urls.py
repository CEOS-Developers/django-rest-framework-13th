from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.postsList),
    path('profiles/', views.profilesList),
    path('users/', views.usersList),
]
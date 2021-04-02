from django.urls import path
from . import views

urlpatterns = [
    path('api/posts/', views.postsList),
    path('api/profiles/', views.profilesList),
    path('api/users/', views.usersList),
]
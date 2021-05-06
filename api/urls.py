from django.urls import path
from api import views

urlpatterns = [
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>', views.PostDetail.as_view())
    ]
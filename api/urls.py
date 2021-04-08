from django.urls import path
from api import views

urlpatterns = [
    path('post/', views.postList.as_view()),
    path('post/<int:pk>', views.postDetail.as_view())
]
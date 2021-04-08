from django.urls import path
from .views import UserList, UserUpload, UploadFix

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/uploads/', UserUpload.as_view()),
    path('uploads/<int:pk>/', UploadFix.as_view()),

]
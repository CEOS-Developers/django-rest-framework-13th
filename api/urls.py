from django.urls import path
from api import views
from .views import UserList

urlpatterns = [
    path('api/', UserList.as_view())
]
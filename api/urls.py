from django.urls import path, include
from . import views
from rest_framework import routers
from .views import ProfileViewSet, PostViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'post', PostViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('login/',views.login)
]

from django.urls import path
from api import views
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'post', PostViewSet)
router.register(r'file', FileViewSet)
router.register(r'follow', FollowViewSet)
router.register(r'heart', HeartViewSet)

urlpatterns = router.urls

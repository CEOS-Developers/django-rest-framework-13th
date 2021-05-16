from rest_framework import routers
from .views import ProfileViewSet, UploadViewSet

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'upload', UploadViewSet)

urlpatterns = router.urls

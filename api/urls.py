from django.urls import path, include
from api import views
from .views import PostViewSet
from rest_framework.routers import DefaultRouter
# CBV
# urlpatterns = [
#     path('post/', views.PostList.as_view()),
#     path('post/<int:pk>', views.PostDetail.as_view())
#     ]

# ViewSet
router = DefaultRouter()
router.register('posts', PostViewSet,basename='posts')
urlpatterns = [
    path('', include(router.urls)),
]

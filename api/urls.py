from django.urls import path
from .views import UserViewSet, PostViewSet
from rest_framework.routers import DefaultRouter

# from .views import UserList, PostList, PostDetail

# user_list = UserViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# post_list = PostViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'posts', PostViewSet)

# urlpatterns = [
#     path('api/users', UserList.as_view(), name='user-list'),
#     path('api/posts', PostList.as_view(), name='post-list'),
#     path('api/posts/<int:pk>', PostDetail.as_view(), name='post-detail')
# ]

urlpatterns = router.urls

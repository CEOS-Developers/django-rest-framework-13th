from rest_framework import permissions


class IsAuthorOrReadonly(permissions.BasePermission):
    # 인증된 유저만 목록 조회/ 포스팅 가능
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # when method is get, head, options always true
        if request.method in permissions.SAFE_METHODS:
            return True
        # only author is allowed for put, delete
        return obj.author == request.user

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = 'Вы можете изменять только свой контент!'

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )

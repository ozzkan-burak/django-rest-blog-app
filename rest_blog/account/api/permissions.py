from rest_framework.permissions import BasePermission


class NotAuthenticated(BasePermission):
    message = 'You are already authenticated'
    def has_object_permission(self, request, view):
        return not request.user and not request.user.isauthenticated
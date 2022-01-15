from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "You are not the owner of this post."
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
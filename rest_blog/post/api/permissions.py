from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view):
        return request.user and request.usr.isauthenticated
    
    message = "You are not the owner of this post."
    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user) or request.user.is_superuser
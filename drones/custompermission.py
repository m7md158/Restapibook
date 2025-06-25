from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # the method is safe, return True
            return True
        else:
            # the method is not safe, return False 
            # only owners are granted permission for unsafe methods
            return obj.owner == request.user
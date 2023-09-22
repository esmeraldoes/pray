# permissions.py

from rest_framework import permissions

class IsSocialAccountOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a social account to access it.
    """

    def has_object_permission(self, request, view, obj):
        
        return obj.user == request.user


from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow users to edit their own profiles.
    """

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True

       
        return obj == request.user.profile

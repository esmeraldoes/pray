# permissions.py

from rest_framework import permissions

class IsSocialAccountOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a social account to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user making the request is the owner of the social account
        return obj.user == request.user


from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow users to edit their own profiles.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the profile
        return obj == request.user.profile

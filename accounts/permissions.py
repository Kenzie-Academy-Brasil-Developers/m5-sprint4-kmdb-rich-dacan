from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # by default, use 'request.user'
        return (obj == request.user) | request.user.is_staff

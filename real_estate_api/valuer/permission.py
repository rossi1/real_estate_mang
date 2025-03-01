from rest_framework.permissions import BasePermission

class IsValuer(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_valuer
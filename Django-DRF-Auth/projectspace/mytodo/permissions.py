from rest_framework.permissions import BasePermission
from rest_framework.response import Response

class IsOwnerOrModerator(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_authenticated and (user.roles.lower() == 'moderator' or obj.owner == user):
            return True
        return False

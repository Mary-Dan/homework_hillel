from rest_framework import permissions
from messenger_project.messenger.models import Message


class IsAuthorOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if isinstance(obj, Message) and obj.author == request.user:
            return True
        return False


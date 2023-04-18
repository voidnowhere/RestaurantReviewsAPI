from rest_framework.permissions import BasePermission

from .models import User


class IsReviewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type == User.REVIEWER

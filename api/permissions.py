from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "Incorrect user matchup"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.profile.user == request.user:
            return True
        return False

class IsUser(BasePermission):
    message = "Incorrect user matchup"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.user == request.user:
            return True
        return False

class IsItemUser(BasePermission):
    message = "Incorrect user matchup"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.order.profile.user == request.user:
            return True
        return False
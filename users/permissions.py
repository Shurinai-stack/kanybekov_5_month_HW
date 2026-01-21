from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """
    Доступ только для сотрудников (модераторов)
    """
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )

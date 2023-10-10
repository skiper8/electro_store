from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    """ Permissions class для пользователей с флагом is_staff """

    message = 'Вы не модератор'

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False


class IsSuperUser(BasePermission):
    """ Permissions class для пользователей с флагом is_superuser """

    message = 'Вы не администратор'

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class IsActive(BasePermission):
    """ Permissions class для пользователей с флагом is_active=True """

    message = 'Обратитесь к администратору для активации аккаунта'

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False


class IsCustomer(BasePermission):
    """ Permissions class для пользователей по параметру supplier """

    message = "Как поставщик вы не можете изменять заказы"

    def has_permission(self, request, view):
        if request.user.supplier is False:
            return True
        return False

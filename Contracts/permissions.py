from rest_framework import permissions


# Permission pour mettre à jour un contrat si on y est affecté
class SalesBindToContractOrReadOnly(permissions.BasePermission):
    message = "Vous pouvez mettre à jour un contrat uniquement si vous y êtes affecté"

    def has_permission(self, request, view):
        return request.user

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.sales_contact_id == request.user.id or request.user.team == 'Management'


# Class permettant à un membre de la team support d'afficher les
# contrats auxquels il est lié
class SupportOrReadOnly(permissions.BasePermission):
    message = "Seul le support peut lire les données"

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.team == 'SUPPORT':
            return False
        return True

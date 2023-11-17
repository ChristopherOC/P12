from rest_framework import permissions


# Permission pour les membres de l'aquipe commerciale
class IsSaleEmployeeOrReadOnly(permissions.BasePermission):
    message = "Seul le commercial affecté au client peut ajouter ou mettre à jour"

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.team == 'SUPPORT':
            return False
        return True

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.sales_contact == request.user

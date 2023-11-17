from rest_framework import permissions

# Permission pour les membres de l'équipe Management
class ManagementPermission(permissions.BasePermission):
    message = "Vous n'avez pas la permission de supprimer cet utilisateur."

    def has_permission(self, request, view):
        return request.user.team in ["Management"]

    def has_object_permission(self, request, view, obj):
        return request.user.team in ["Management"]

from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from datetime import datetime, timezone


# Permission pour afficher les évènements
class EventPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            # Autoriser la lecture pour tout le monde
            return True
        if request.method == "POST":
            # Autorise la création d'événements pour les membres de l'équipe commerciale
            return request.user.team == "Sales"
        return False


# Permission pour mettre à jour un évènement
class EventUpdatePerm(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.event_status == 4:
            # Si le statut de l'événement = terminé, interdit toute modification
            raise PermissionDenied("Impossible de mettre à jour un événement terminé.")

        if obj.event_date < datetime.now(timezone.utc):
            raise PermissionDenied("Impossible de mettre à jour un événement passé.")

        if request.user.team == "Support":
            # Vérifier si l'utilisateur de l'équipe "Support" est le support_contact de l'événement
            return request.user.id == obj.support_contact_id
        if request.user.team == "Management":
            return True
        return False

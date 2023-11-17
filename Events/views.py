from rest_framework import viewsets
from Events.serializers import EventSerializers
from Events.models import Event
from rest_framework.permissions import IsAuthenticated
from Events.permissions import EventPermissions, EventUpdatePerm


# Vue pour afficher les évènements
class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializers
    permission_classes = [IsAuthenticated, EventPermissions]


# Vue permettant de mettre à jour un évènement
class EventUpdate(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializers
    permission_classes = [IsAuthenticated, EventUpdatePerm]


# Vue permettant à un support d'afficher les évènements auxquels il est lié
class SupportOfTheEvent(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.team == "Support":
            return Event.objects.filter(support_contact=user)
        else:
            return Event.objects.none()

from rest_framework import serializers
from Events.models import Event


# Serializer d'un évènement pour la BDD
class EventSerializers(serializers.ModelSerializer):

    class Meta:

        model = Event
        fields = ['id',
                  'name',
                  'contract',
                  'date_created',
                  'date_updated',
                  'support_contact',
                  'event_date',
                  'participants',
                  'notes',
                  'event_status']

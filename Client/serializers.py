from rest_framework import serializers
from .models import Client


# Serializer d'un client pour la BDD
class ClientSerializer(serializers.ModelSerializer):

    class Meta:

        model = Client
        fields = ["id",
                  "first_name",
                  "last_name",
                  "email",
                  "phone",
                  "mobile",
                  "company_name",
                  "date_created",
                  "date_updated",
                  "sales_contact"
                  ]

    def create(self, validated_data):
        # Récupère l'utilisateur actuel à partir de la demande
        request = self.context.get('request')
        user = request.user if request else None

        if user and user.team == 'Sales':
            validated_data["sales_contact"] = user

        instance = Client(**validated_data)
        instance.save()
        return instance

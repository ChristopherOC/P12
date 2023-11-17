from rest_framework import serializers
from Contracts.models import Contract


# Serialiseur des contrats avec les champs pour la BDD
class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id',
                  'sales_contact',
                  'client',
                  'date_created',
                  'date_updated',
                  'status',
                  'amount',
                  'remaining_payment',
                  'payment_due']

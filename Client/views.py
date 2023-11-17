from rest_framework import viewsets
from Client.models import Client
from Client.serializers import ClientSerializer
from Client.permissions import IsSaleEmployeeOrReadOnly
from rest_framework.permissions import IsAuthenticated


# Vue permettant la création d'un client
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsSaleEmployeeOrReadOnly]

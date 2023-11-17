from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from Contracts.models import Contract
from Contracts.serializers import ContractSerializer
from Contracts.permissions import SalesBindToContractOrReadOnly, SupportOrReadOnly


# Vue permettatn l'affichange des contrats
class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated,
                          SalesBindToContractOrReadOnly,
                          SupportOrReadOnly]


#Vue n'affichant que les contrats non totalement reglés
class UnpaidContractsViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()

    def get_queryset(self):
        # Vue accessible uniquement par l'équipe "Sales".
        if self.request.user.team != "Sales":
            return Contract.objects.none()

        # Requête pour récupérer les contrats non payés.
        return Contract.objects.filter(sales_contact=self.request.user, remaining_payment__gt=0)

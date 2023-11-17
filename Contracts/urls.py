from rest_framework import routers
from Contracts.views import ContractViewSet, UnpaidContractsViewSet
from django.urls import path
router = routers.DefaultRouter()
router.register('contract', ContractViewSet)
router.register('unpaid-contract', UnpaidContractsViewSet)

urlpatterns = {
    path('contract/<int:pk>/', ContractViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'}), name='contract-detail'),
}

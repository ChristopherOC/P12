import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from Client.models import Client
from Contracts.models import Contract

@pytest.mark.django_db
def test_sales_member_can_create_contract():
    client = APIClient()

    # Création d'un utilisateur de test dans l'équipe des ventes
    management_user_data = {
        "username": "Mana_test_user",
        "password": "test_pwd",
        "team": "Management",
    }
    management_user = get_user_model().objects.create_user(**management_user_data)

    # Création d'un client
    client_data = {
        "first_name": "Kamel",
        "last_name": "Kebir",
        "email": "fake@mail.co",
        "phone": "1234567890",
        "mobile": "9876543210",
        "company_name": "Karmine Corp",
        "sales_contact": management_user,
    }
    client_object = Client.objects.create(**client_data)

    # Connexion
    client.force_authenticate(user=management_user)

    # Création du contrat
    create_contract_url = reverse("contract-list")

    # Données du contrat
    new_contract_data = {
        "client": client_object.id,
        "amount": "10000.00",
        "remaining_payment": "10000.00",
    }

    # Création d'un contrat en tant que membre commercial
    response = client.post(create_contract_url, new_contract_data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Contract.objects.filter(client=client_object, amount="10000.00").exists()

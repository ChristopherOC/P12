import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from Client.models import Client

@pytest.mark.django_db
def test_sales_member_can_create_client():
    client = APIClient()

    # Création d'un utilisateur dans l'équipe des ventes
    sales_user_data = {
        "username": "sale_user",
        "password": "sale_password",
        "team": "Sale",
    }
    sales_user = get_user_model().objects.create_user(**sales_user_data)

    # Connexion
    client.force_authenticate(user=sales_user)

    # Endpoint pour créer un client
    create_client_url = reverse("client-list")

    # Données du client
    new_client_data = {
        "first_name": "Kamel",
        "last_name": "Kebir",
        "email": "fakemail@fake.co",
        "phone": "1234567890",
        "mobile": "9876543210",
        "company_name": "Karmine Corp",
    }

    # Création du client
    response = client.post(create_client_url, new_client_data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Client.objects.filter(first_name="Kamel", last_name="Kebir").exists()


@pytest.mark.django_db
def test_sales_member_can_update_own_clients_data():
    client = APIClient()

    # Création d'un utilisateur dans l'équipe des ventes
    sales_user_data = {
        "username": "sale_user",
        "password": "sale_password",
        "team": "Sales"
    }
    sales_user = get_user_model().objects.create_user(**sales_user_data)

    # Création client avec utilisateur des ventes comme contact commercial
    client_to_update_data = {
        "first_name": "Kamel",
        "last_name": "Kebir",
        "email": "fakemail@fake.co",
        "phone": "1234567890",
        "mobile": "9876543210",
        "company_name": "Karmine Corp",
        "sales_contact": sales_user,
    }
    client_to_update = Client.objects.create(**client_to_update_data)

    # Connexion
    client.force_authenticate(user=sales_user)

    # Mis à jour du client
    update_client_url = reverse("client-detail", kwargs={"pk": client_to_update.id})

    # Nouvelles données client
    updated_client_data = {
        "first_name": "Updated Kamel",
        "last_name": "Updated Kebir",
        "email": "fakemail@fake.co",
    }

    # Mis à jour du client en étant le sales_contact
    response = client.patch(update_client_url, updated_client_data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert Client.objects.filter(first_name="Updated Kamel", last_name="Updated Kebir").exists()

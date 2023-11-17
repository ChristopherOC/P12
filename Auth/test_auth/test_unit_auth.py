import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from Auth.models import MyCustomUser
from django.contrib.auth import get_user_model



@pytest.mark.django_db
def test_user_login():
    client = APIClient()

    # Données de l'user a connecter
    user_data = {
        "username": "username1",
        "password": "password1",
    }
    user = MyCustomUser.objects.create_user(**user_data)

    # Connexion
    login_url = reverse("login")
    response = client.post(login_url, {"username": "username1", "password": "password1"}, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_user_creation_as_manager():
    client = APIClient()

    # Création d'un utilisateur gestion
    manager_data = {
        "username": "test_manager",
        "password": "testpwd",
        "team": "Management",
    }
    manager = MyCustomUser.objects.create_user(**manager_data)

    # Connexion
    client.force_authenticate(user=manager)
    create_user_url = reverse("create")

    # Création d'un nouvel user
    new_user_data = {
        "username": "new_user",
        "password": "new_password",
        "first_name": "demonstration",
        "last_name": "demo",
        "email": "emailed@example.com",
        "team": "Sale",
    }
    response = client.post(create_user_url, new_user_data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert MyCustomUser.objects.filter(username="new_user").exists()

@pytest.mark.django_db
def test_management_user_can_delete_user():
    client = APIClient()

    # Création d'un user de l'équipe gestion
    manager_data = {
        "username": "manager_user",
        "password": "manager_password",
        "team": "Management",
    }
    manager = get_user_model().objects.create_user(**manager_data)

    # Création de l'user a supprimer
    user_to_delete_data = {
        "username": "test_delete",
        "password": "deletepwd",
        "team": "Sales",
    }
    user_to_delete = get_user_model().objects.create_user(**user_to_delete_data)

    # Connexion en tant que membre gestion
    client.force_authenticate(user=manager)

    # Suppression de l'user créé
    delete_user_url = reverse("delete-user", kwargs={"pk": user_to_delete.id})
    response = client.delete(delete_user_url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not get_user_model().objects.filter(id=user_to_delete.id).exists()
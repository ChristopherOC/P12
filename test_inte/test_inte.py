import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status


@pytest.mark.django_db
class TestAuthIntegration:

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def initial_users(self):
        # Création de l'user
        MyCustomUser = get_user_model()
        users = [
            MyCustomUser.objects.create_user(
                username='username1',
                first_name='Jean',
                last_name='famille',
                password='password1',
                email='fakemail1@fake.com',
                team='Management'
            ),
        ]
        return users

    def test_integration_create_and_delete(self, api_client, initial_users):
        # Vérification de la création des users
        assert len(initial_users) == 1

        # Connexion avec l'user
        user_to_login = initial_users[0]
        login_data = {
            'username': user_to_login.username,
            'password': 'password1',
        }
        response = api_client.post('/api/auth/login/', data=login_data)
        assert response.status_code == status.HTTP_200_OK
        print("logged")

        # Création d'un nouvel user
        new_user_data = {
            "username": "new_user",
            "password": "new_password",
            "first_name": "demonstration",
            "last_name": "demo",
            "email": "emailed@example.com",
            "team": "Sale",
        }
        api_client.force_authenticate(user=user_to_login)
        response = api_client.post('/api/auth/create/', data=new_user_data)
        assert response.status_code == status.HTTP_201_CREATED
        print("created")

        # Suppression de l'user créé
        new_user_id = response.data.get('id')
        print("new_user_id", new_user_id)
        response = api_client.delete(f'/api/auth/delete_user/{new_user_id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT

        assert not get_user_model().objects.filter(id=new_user_id).exists()

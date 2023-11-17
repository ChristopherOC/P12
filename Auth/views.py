from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, DestroyAPIView
from .models import MyCustomUser
from .serializers import UserSerializer
from .permissions import ManagementPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


# Classe permettant la créations d'un nombre d'utilisateur générique
class CreateInitialUsersView(APIView):
    def post(self, request):
        MyCustomUser = get_user_model()

        # Vérifiez si les utilisateurs existent déjà
        if not MyCustomUser.objects.filter(id=1).exists():
            MyCustomUser.objects.create_user(
                username='username1',
                first_name='Jean',
                last_name='famille',
                password='password1',
                email='fakemail1@fake.com',
                team='Sales'
            )

        if not MyCustomUser.objects.filter(id=2).exists():
            MyCustomUser.objects.create_user(
                username='username2',
                first_name='Kyllian',
                last_name='Mbappé',
                password='password2',
                email='fakemail2@fake.com',
                team='Sales'
            )

        if not MyCustomUser.objects.filter(id=3).exists():
            MyCustomUser.objects.create_user(
                username='username3',
                first_name='Paul',
                last_name='Seul',
                password='password3',
                email='fakemail3@fake.com',
                team='Management'
            )

        if not MyCustomUser.objects.filter(id=4).exists():
            MyCustomUser.objects.create_user(
                username='username4',
                first_name='Cédric',
                last_name='Doumbé',
                password='password4',
                email='fakemail4@fake.com',
                team='Support'
            )

        if not MyCustomUser.objects.filter(id=5).exists():
            MyCustomUser.objects.create_user(
                username='username5',
                first_name='Cyril',
                last_name='Gane',
                password='password5',
                email='fakemail5@fake.com',
                team='Support'
            )

        return Response({"message": "Utilisateurs créés avec succès"}, status=status.HTTP_201_CREATED)


# Vue permettant la création d'utilisateur
class UserCreation(CreateAPIView):
    queryset = MyCustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.team == "Management":
            serializer.save()
        else:
            raise PermissionDenied("Seul les membres de l'équipe Gestion peuvent effectuer ceci")

# Vue permettant la suppression d'utilisateur de la BDD
class DeletingUsers(DestroyAPIView):
    queryset = MyCustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ManagementPermission]

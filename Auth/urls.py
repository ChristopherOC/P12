from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CreateInitialUsersView, UserCreation, DeletingUsers

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("login/token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path('create_initial_users/', CreateInitialUsersView.as_view(), name='create_initial_users'),
    path('create/', UserCreation.as_view(), name='create'),
    path('delete_user/<int:pk>/', DeletingUsers.as_view(), name='delete-user')
]
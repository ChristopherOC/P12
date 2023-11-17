from rest_framework import routers
from Client.views import ClientViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register('client', ClientViewSet)

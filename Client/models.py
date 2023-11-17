from django.db import models
from django.conf import settings
from django.db.models.deletion import RESTRICT


# Class model d'un client
class Client(models.Model):

    objects = None
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=80)
    phone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    company_name = models.CharField(max_length=80)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=RESTRICT,
                                      related_name="client_assigned_to",
                                      null=True,
                                      blank=True
                                      )

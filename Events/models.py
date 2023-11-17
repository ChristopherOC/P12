from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from django.conf import settings
from Contracts.models import Contract

# Create your models here.

# Class model d'un évènement
class Event(models.Model):

    # Choix des status possibles
    CHOICES_STATUS = (
        (1, 'Not attributed'),
        (2, 'Begin'),
        (3, 'In Progress'),
        (4, 'Ended')
        )
    
    event_status = models.PositiveSmallIntegerField(choices=CHOICES_STATUS, verbose_name="Status", default=1)
    name = models.CharField(max_length=100)
    contract = models.ForeignKey(Contract,
                                 on_delete=CASCADE,
                                 related_name="test",
                                 null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=RESTRICT,
                                        related_name="event_assigned_to",
                                        null=True)

    participants = models.IntegerField(default=0)
    event_date = models.DateTimeField()
    notes = models.TextField(max_length=500)

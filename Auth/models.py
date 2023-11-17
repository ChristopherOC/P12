from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User Model with a team Choices
class MyCustomUser(AbstractUser):
    team_choices = [('Management', 'Gestion'),
                    ('Support', 'Support'),
                    ('Sale', 'Vente')]

    team = models.CharField(max_length=40, choices=team_choices, blank=True)

    def save(self, *args, **kwargs):
        if self.team_choices == 'Management':
            self.is_admin = True

        return super(MyCustomUser, self).save(*args, **kwargs)

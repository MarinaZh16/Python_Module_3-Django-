from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid as uuid


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    token = models.CharField(max_length=32, blank=True, null=True)
    email_confirmed = models.BooleanField(default=False)
    active_from = models.DateTimeField(blank=True, null=True)
    wallet = models.FloatField(default=10000, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        if not self.token:
            self.token = str(uuid.uuid4()).replace('-', '')
        if self.is_superuser:
            self.wallet = 0
        return super(User, self).save(*args, **kwargs)

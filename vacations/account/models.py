from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    is_manager = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk) + " -- " + self.username

    class Meta:
        ordering = ['created']

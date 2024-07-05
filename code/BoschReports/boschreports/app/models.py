from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    edv = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

class Reports(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    identified_ris = models.CharField(max_length=100)
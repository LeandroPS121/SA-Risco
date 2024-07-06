from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    edv = models.CharField(max_length=8, unique=True)
    last_name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.username    

class Reports(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    planta_reports = models.CharField(max_length=100)
    sala_reports = models.CharField(max_length=100)
    situacao_reports = models.CharField(max_length=255)
    risco_identificado_reports = models.CharField(max_length=255)
    houve_vitimas_reports = models.BooleanField(default=False)
    nivel_danos_reports = models.CharField(max_length=50)
    descricao_reports = models.TextField(blank=True, null=True)
    

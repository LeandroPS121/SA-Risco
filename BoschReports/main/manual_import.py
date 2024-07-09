# Importe o modelo e as configurações do Django
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from app.models import Planta,Local

def adicionar_planta(nome, pais, estado, cidade):
    planta = Planta(nome_planta=nome, pais_planta=pais, estado_planta=estado,cidade_planta=cidade)
    planta.save()

def adicionar_local(nome, planta_id):
    planta = Planta.objects.get(id=planta_id)
    
    local = Local(nome_local=nome, planta=planta)
    local.save()

adicionar_local('Estacionamento',1)
adicionar_local('Entrada',1)
adicionar_local('Banheiro Masculino',1)
adicionar_local('Banheiro Feminino',1)
adicionar_local('Copa',1)
adicionar_local('Sala DTA',1)
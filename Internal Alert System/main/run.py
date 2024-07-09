# Importe o modelo e as configurações do Django
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from app.models import Planta,Local,Reports,Situacao

def adicionar_planta(nome, pais, estado, cidade):
    planta = Planta(nome_planta=nome, pais_planta=pais, estado_planta=estado,cidade_planta=cidade)
    planta.save()

def adicionar_local(nome, planta_id):
    planta = Planta.objects.get(id=planta_id)
    
    local = Local(nome_local=nome, planta=planta)
    local.save()

def adicionar_situacao(local_id,nome,descricao):
    situacao=Situacao(local=Local.objects.get(id=local_id),nome_situacao=nome,descricao_situacao=descricao)
    situacao.save()

# adicionar_situacao(6,'Sistema de ventilação e ar condicionado defeituoso','Um sistema de ventilação e ar condicionado defeituoso '
#                    +'impede a regulação eficaz da temperatura e da qualidade do ar, impactando adversamente o conforto e a saúde dos usuários do espaço.')
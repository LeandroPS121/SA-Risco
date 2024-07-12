import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Reports, CustomUser,Planta,Local,Situacao,Risco
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import json


CustomUser = get_user_model()

def register_view(request):
    
    if request.method == 'POST':
        edv_reg = request.POST.get('edv')
        first_name_reg = request.POST.get('nome')
        last_name_reg = request.POST.get('sobrenome')
        password_reg = request.POST.get('senha')
        email_reg = request.POST.get('email')

        # Verifica se o usuário com o EDV já existe
        if CustomUser.objects.filter(edv=edv_reg).exists():
            return render(request, 'app/register.html', {'erro': True})

        # Cria um novo usuário
        user = CustomUser.objects.create_user(
            username=str(last_name_reg + '_' + first_name_reg + '_'+ edv_reg),
            first_name=first_name_reg,
            edv=edv_reg,
            last_name=last_name_reg,
            password=password_reg,
            email=email_reg
        )
        
        return redirect('login')

    return render(request, 'app/register.html')




def main_admin_view(request):
    data = Reports.objects.all()
    return render(request,'app/main.html',{'reports':data})




def redirect_login_view(request):
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        edv = request.POST.get('edv')
        password = request.POST.get('password')
        print('edv: '+edv+'\nsenha: '+password)
        
        user = authenticate(request, edv=edv, password=password)
            
        if user is not None:
            # Login bem-sucedido
            login(request, user)

            verify_admin(request)

            return redirect('form')  # Redirecionar para a página principal
        else: 
            return render(request, 'app/login.html',{'erro':True})
    else:
        # Se não for um POST, renderizar a página de login
        return render(request, 'app/login.html')
    

def logout_view(request):
    logout(request)
    return redirect('login')

def form_view(request):
    
    if request.method == 'POST':           
        # Cria um novo objeto Reports e salva no banco de dados


        report = Reports.objects.create(
        user=request.user,
        planta_reports = request.POST.get('planta'),
        local_reports = request.POST.get('local'),
        situacao_reports=request.POST.get('situacao'),
        risco_identificado_reports=request.POST.get('riscoIdentificado'),
        houve_vitimas_reports=request.POST.get('houveVitimas'),
        nivel_danos_reports=request.POST.get('nivelDanos'),
        area_responsavel_reports=request.POST.get('areaResponsavel'),
        descricao_reports='teste'
        )
        report.save()
        
        return redirect('success')  # Redireciona para uma página de successo após salvar
    else:
        
        plantas=Planta.objects.all()

        return render(request, 'app/form.html',{'plantas':plantas}) 

def form_success_view(request):
    return render(request,'app/success.html')

def verify_admin(request):
    if request.user.is_superuser==True:
        return redirect('main')
    


def form_load_locals(request):
    if request.method == 'POST':

            data = json.loads(request.body)
            
            planta_id = data.get('planta_id')

            print('id local: '+planta_id)
            
            locals = Local.objects.filter(planta=planta_id).values('id', 'nome_local')
            
            return JsonResponse({'locals': list(locals)})
    
    else:
        plantas=Planta.objects.all()
        return render(request, 'app/form.html',{'plantas':plantas})
    




    
def form_load_situacoes(request):
    if request.method == 'POST':

            data = json.loads(request.body)
            
            local_id = data.get('local_id')
            
            situacoes = Situacao.objects.filter(local=local_id).values('id', 'nome_situacao','verifica_area_situacao')
            
            return JsonResponse({'situacoes': list(situacoes)})
    
    else:
        plantas=Planta.objects.all()
        return render(request, 'app/form.html',{'plantas':plantas})
    
    
def form_load_riscos(request):
    if request.method == 'POST':

            data = json.loads(request.body)
            
            situacao_id = data.get('situacao_id')

            print("id situacao: "+situacao_id)
            
            riscos = Risco.objects.filter(situacao=situacao_id).values('id', 'nome_risco','verifica_area_risco')
            
            return JsonResponse({'riscos': list(riscos)})
    
    else:
        plantas=Planta.objects.all()
        return render(request, 'app/form.html',{'plantas':plantas})
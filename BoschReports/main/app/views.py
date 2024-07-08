from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Reports, CustomUser
from django.contrib.auth import get_user_model

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
            username=str(last_name_reg + '_' + first_name_reg),
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
            print(f'Usuário encontrado no banco - edv: {user.edv}, username: {user.username}')
        else:
            print('Usuário não encontrado no banco.')
            
        if user is not None:
            # Login bem-sucedido
            login(request, user)
            return redirect('main')  # Redirecionar para a página principal
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
        print('1')
        # Cria um novo objeto Reports e salva no banco de dados
        report = Reports.objects.create(
            user=request.user,
            planta_reports=request.POST.get('planta'),
            sala_reports=request.POST.get('sala'),
            situacao_reports=request.POST.get('situacao'),
            risco_identificado_reports=request.POST.get('risco_identificado'),
            houve_vitimas_reports=request.POST.get('houveVitimas'),
            nivel_danos_reports=request.POST.get('nivel_danos'),
            descricao_reports='teste',
        )
        print('2')
        report.save()
        print('3')
        
        return redirect('success')  # Redireciona para uma página de successo após salvar
    else:
        print('nao eh posto')
        return render(request, 'app/form.html')

def form_success_view(request):
    return render(request,'app/success.html')
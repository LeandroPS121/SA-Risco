from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Reports, CustomUser
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

def register_view(request):
    if request.method == 'POST':
        edv_register = request.POST.get('edv')
        first_name = request.POST.get('nome')
        last_name = request.POST.get('sobrenome')
        password = request.POST.get('senha')
        email = request.POST.get('email')

        if CustomUser.objects.filter(edv=edv_register).exists():
         
            return render(request, 'app/register.html', {'error_message': 'Usuário já existe. Escolha outro nome.'})

        user = CustomUser.objects.create_user(username=str(last_name+'_'+first_name),first_name=first_name, edv=edv_register, last_name=last_name, password=password, email=email)

        return redirect('login')

    return render(request, 'app/register.html')

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
            return render(request,'app/main.html')  # Redirecionar para a página principal
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
            # Cria ou atualiza o objeto Reports para o usuário atual
        obj = Reports.objects.filter()
        palnta=request.get('planta')
        sala= request.get('sala')
        situacao=request.get('situacao')
        risco_identificado=request.get('risco_identificado')
        houve_vitimas=request.get('houveVitimas')
        nivel_danos=request.get('nivel_danos')
        descricao=request.get('descricao')
        
        return redirect('pagina_de_sucesso')  # Redireciona para uma página de sucesso após salvar
    else:
    
        return render(request, 'app/form.html')

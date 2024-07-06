from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm, ReportForm
from .models import Reports, CustomUser
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

def register_view(request):
    if request.method == 'POST':
        edv = request.POST.get('edv')
        first_name = request.POST.get('nome')
        last_name = request.POST.get('sobrenome')
        password = request.POST.get('senha')
        email = request.POST.get('email')

        # Validar os dados recebidos

        # Verificar se já existe um usuário com o mesmo nome
        if CustomUser.objects.filter(username=str(first_name+'_'+last_name)).exists():
            # Tratar o erro de usuário já existente
            return render(request, 'app/register.html', {'error_message': 'Usuário já existe. Escolha outro nome.'})

        # Criar um novo usuário CustomUser
        user = CustomUser.objects.create_user(username=str(first_name+'_'+last_name),first_name=first_name, edv=edv, last_name=last_name, password=password, email=email)

        # Redirecionar para a página de login após o registro
        return redirect('login')

    # Renderizar o template de registro normalmente para o método GET
    return render(request, 'app/register.html')

def redirect_login_view(request):
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = UserLoginForm()
    return render(request, 'app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def form_view(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            # Cria ou atualiza o objeto Reports para o usuário atual
            obj = Reports.objects.update_or_create(
                user=request.user,
                defaults={
                    'planta_reports': form.cleaned_data.get('planta'),
                    'sala_reports': form.cleaned_data.get('sala'),
                    'situacao_reports': form.cleaned_data.get('situacao'),
                    'risco_identificado_reports': form.cleaned_data.get('risco_identificado'),
                    'houve_vitimas_reports': form.cleaned_data.get('houveVitimas'),
                    'nivel_danos_reports': form.cleaned_data.get('nivel_danos'),
                    'descricao_reports': form.cleaned_data.get('descricao'),
                }
            )
            return redirect('pagina_de_sucesso')  # Redireciona para uma página de sucesso após salvar
    else:
        form = ReportForm()
    
    return render(request, 'app/form.html', {'form': form})

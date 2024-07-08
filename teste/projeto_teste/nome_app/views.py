from django.shortcuts import render, redirect
from .models import Frequencia
from .forms import FrequenciaForm

def registrar_presenca(request):
    if request.method == 'POST':
        form = FrequenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabela_frequencia')
    else:
        form = FrequenciaForm()

    return render(request, 'nome_app/registrar_presenca.html', {'form': form})

def tabela_frequencia(request):
    frequencias = Frequencia.objects.all()
    return render(request, 'nome_app/tabela_frequencia.html', {'frequencias': frequencias})
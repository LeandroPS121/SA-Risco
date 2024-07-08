from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nome_app.urls')),  # substitua 'nome_app' pelo nome do seu aplicativo
    path('registrar/', include('nome_app.urls')),  # inclua as rotas do seu aplicativo, se necessário
    path('tabela/', include('nome_app.urls')),  # inclua as rotas do seu aplicativo, se necessário
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view),
    path('form/',views.form_view, name='form'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('main/',views.main_admin_view, name='main'),
    path('form/success/',views.form_success_view,name='success')
]


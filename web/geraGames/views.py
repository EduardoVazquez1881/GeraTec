from django.shortcuts import render
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def prueba(request):
    return render(request, 'prueba.html')

def info(request):
    return render(request, 'info.html')

def login(request):
    return render(request, 'login.html')

def menu(request):
    return render(request, 'menu.html')

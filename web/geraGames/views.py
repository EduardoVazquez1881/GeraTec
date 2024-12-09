from django.shortcuts import render
from .models import Usuario, Juego, JuegosDatos

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
    datosgames = JuegosDatos.objects.select_related('juego', 'creador').prefetch_related('categoria', 'plataforma')
    juegos = Juego.objects.all()  # Todos los juegos
    return render(request, 'menu.html', {'datosgames': datosgames, 'juegos': juegos})

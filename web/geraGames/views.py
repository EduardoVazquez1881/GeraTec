from django.shortcuts import render, get_object_or_404
from .models import Usuario, Juego, JuegosDatos, Review
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def prueba(request):
    return render(request, 'prueba.html')

def info(request):
    return render(request, 'info.html')

def login(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        contra = request.POST['contra']

        try:
            usuario = Usuario.objects.get(correo=correo)

            if usuario.contra == contra:
                return redirect('/menu')  # Redirige al inicio
            else:
                return render(request, 'login.html', {'error': 'Contraseña incorrecta'})
        except Usuario.DoesNotExist:
            return render(request, 'login.html', {'error': 'Usuario no encontrado'})

    return render(request, 'login.html')

def registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre1']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        contra = request.POST['contra']

        if Usuario.objects.filter(correo=correo).exists():
            messages.error(request, 'El correo ya está registrado')
            return redirect('/registro')
        
        Usuario.objects.create(nombre=nombre, apellido=apellido, correo=correo, contra=contra)
        messages.success(request, 'Usuario registrado con éxito')


        return redirect('/login')
    return render(request, 'registro.html')    
        

def menu(request):
    datosgames = JuegosDatos.objects.select_related('juego', 'creador').prefetch_related('categoria', 'plataforma')
    juegos = Juego.objects.all()  # Todos los juegos
    juegosvisitados = Juego.objects.order_by('-visitas')[:5]  # Los 5 juegos más visitados
    print(juegos)
    return render(request, 'menu.html', {'datosgames': datosgames, 'juegos': juegos, juegosvisitados: 'juegosvisitados'})

def info(request, juego_id):
    #if request.method == 'POST':
        
    juego = get_object_or_404(Juego, pk=juego_id)
    juego.visitas += 1
    juego.save()

    obj = JuegosDatos.objects.get(juego=juego)
    creadores = obj.creador
    plataformas = obj.plataforma.all()
    categorias = obj.categoria.all()


    total= 0
    res = Review.objects.filter(juego=juego)
    if (res.count() != 0):
        calificaciones = [res.calificacion for res in res]
        for i in calificaciones:
            total += i
        total = total / len(calificaciones)

    return render(request, 'info.html', {'juego': juego, 'creadores': creadores, 'plataformas': plataformas, 'categorias': categorias, 'res': res, 'total': total})


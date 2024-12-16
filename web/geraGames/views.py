from django.shortcuts import render, get_object_or_404
from .models import Usuario, Juego, JuegosDatos, Review, Categoria
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date



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
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nombre'] = usuario.nombre
                return redirect('/menu') 
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
    ordenados = datosgames.order_by('-juego__visitas')
    categorias = Categoria.objects.all()
    JuegosCategorias = datosgames.filter(categoria__in=categorias)

    usuario_id = request.session.get('usuario_id')
    print(usuario_id)


    juegosFiltrados = {}
    for i in categorias:
        juegosFiltrados[i.categoria] = datosgames.filter(categoria=i)
        
    return render(request, 'menu.html', {'datosgames': datosgames, 'datosordenados': ordenados, 'categorias': categorias, 'juegosFiltrados': juegosFiltrados, 'JuegosCategorias': JuegosCategorias})




def info(request, juego_id):

    if request.method == 'POST':
        calificacion = request.POST['calificacion']
        dificultad = request.POST['dificultad']
        res = request.POST['res']
        fecha = date.today()
        usuario_id = request.session.get('usuario_id')

        if usuario_id == None:
            return render(request, 'login.html')
        
        filtro = Review.objects.filter(juego_id=juego_id, usuario_id=usuario_id)
        if filtro.count() == 0:
            Review.objects.create(juego_id=juego_id, calificacion=calificacion, dificultad=dificultad, res=res, fecha=fecha, usuario_id=usuario_id)
        else:
            print('Ya has hecho una review')
            
    juego = get_object_or_404(Juego, pk=juego_id)
    juego.visitas += 1
    juego.save()

    obj = JuegosDatos.objects.get(juego=juego)
    creadores = obj.creador
    plataformas = obj.plataforma.all()
    categorias = obj.categoria.all()

    print(juego.visitas)
    total= 0
    res = Review.objects.filter(juego=juego)
    if (res.count() != 0):
        calificaciones = [res.calificacion for res in res]
        for i in calificaciones:
            total += i
        total = total / len(calificaciones)            
    return render(request, 'info.html', {'juego': juego, 'creadores': creadores, 'plataformas': plataformas, 'categorias': categorias, 'res': res, 'total': total})

def categoria(request):
    categoria = request.GET.get('categoria')
    categoria_obj = Categoria.objects.get(categoria=categoria)
    datosgames = JuegosDatos.objects.select_related('juego', 'creador').prefetch_related('categoria', 'plataforma')
    juegos = datosgames.filter(categoria=categoria_obj)

    print(juegos)
    return render(request, 'categorias.html', {'categoria': categoria_obj, 'juegos': juegos})

def cerrar(request):
    request.session.flush()
    return redirect('/menu')


def perfil(request):
    usuario_id = request.session.get('usuario_id')
    usuario = Usuario.objects.get(id=usuario_id)
    imagen = usuario.imagen

    return render(request, 'perfil.html', {'usuario': usuario, 'imagen': imagen})

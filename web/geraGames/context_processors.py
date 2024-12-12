from .models import Categoria, Usuario


def categorias(request):
    categorias = Categoria.objects.all()
    usuario_id = request.session.get('usuario_id')
    usuario =Usuario.objects.get(id=usuario_id)
    fotousuario = usuario.imagen
    print(usuario_id)
    return {'categorias': categorias, 'usuario_id': usuario_id, 'fotousuario': fotousuario}



from .models import Categoria, Usuario
from django.shortcuts import redirect

def categorias(request):
        categorias = Categoria.objects.all()
        
        if request.session.get("usuario_id"):  
            usuario_id = request.session.get('usuario_id')
            
            try:
                usuario = Usuario.objects.get(id=usuario_id)
                fotousuario = usuario.imagen  
            except Usuario.DoesNotExist:

                usuario = None
                fotousuario = None

            return {'categorias': categorias, 'usuario_id': usuario_id, 'fotousuario': fotousuario}
        
        else:
            return {'categorias': categorias}






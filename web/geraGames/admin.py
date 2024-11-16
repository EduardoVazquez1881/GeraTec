from django import forms
from django.contrib import admin
from geraGames.models import Usuario, Categoria, Plataforma, Creador, Juego, Review, JuegosDatos

class JuegosDatosForm(forms.ModelForm):
    categoria = forms.ModelMultipleChoiceField(  # Permite seleccionar múltiples categorías
        queryset=Categoria.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Muestra como checkboxes
        required=True
    )
    plataforma = forms.ModelMultipleChoiceField(  # Permite seleccionar múltiples plataformas
        queryset=Plataforma.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Muestra como checkboxes
        required=True
    )

    class Meta:
        model = JuegosDatos
        fields = ['juego', 'categoria', 'plataforma', 'creador']
# Registrar el admin con el formulario personalizado
class JuegosDatosAdmin(admin.ModelAdmin):
    form = JuegosDatosForm

# Registrar los modelos en el admin
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Plataforma)
admin.site.register(Creador)
admin.site.register(Juego)
admin.site.register(Review)
admin.site.register(JuegosDatos, JuegosDatosAdmin)  # Usamos el admin personalizado

from django.db import models
from django.contrib.auth.models import User

class Categoria (models.Model):
    categoria = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.categoria}"
    
class Plataforma (models.Model):
    palaforma = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.palaforma}"

class Creador(models.Model):
    desarrollador = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.desarrollador}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(unique=True)
    contra = models.CharField(max_length=30)
    super = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='usr/', null=True, blank=True, default='usr/default.jpg')  # Campo para la imagen


    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.correo})"

class Juego(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='juegos/', null=True, blank=True)  # Campo para la imagen
    visitas = models.IntegerField(default=0)
    url = models.URLField(default='', blank=True)  # Define un valor predeterminado para el nuevo campo

    def __str__(self):
        return f"{self.nombre} ({self.precio})"

class Review(models.Model):
    res = models.TextField()
    calificacion = models.IntegerField()
    dificultad = models.IntegerField()
    fecha = models.DateField()
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.res} ({self.calificacion})"
    
class JuegosDatos(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)
    plataforma = models.ManyToManyField(Plataforma)
    creador = models.ForeignKey(Creador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.juego} ({self.categoria})"


    # Create your models here.

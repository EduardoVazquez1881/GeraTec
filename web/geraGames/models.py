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

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.correo})"

class Juego(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    fecha = models.DateField()

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

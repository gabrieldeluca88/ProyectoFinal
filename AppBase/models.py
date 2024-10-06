from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TIPO_OPCIONES = [('nafta', 'Nafta'), ('diesel', 'Diesel'), ('electrico', 'Electrico'), ('hibrido', 'Hibrido'),]

TIPO_OPCIONES = sorted(TIPO_OPCIONES, key=lambda x: x[1])

VALORACIONES_OPCIONES = [(i, str(i)) for i in range(1, 11)]

class Auto(models.Model):
    modelo = models.CharField(max_length=255)
    fecha_salida = models.DateField()
    tipo = models.CharField(max_length=255, choices=TIPO_OPCIONES)
    marca = models.CharField(max_length=255)
    descripcion = models.TextField()
    valoracion = models.IntegerField(choices=VALORACIONES_OPCIONES, null=False)
    def __str__(self):
        return f"{self.modelo} - {self.tipo} - {self.marca}"

class Resena(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.autor} - {self.auto.modelo}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} / {self.imagen}"
    
class Tema(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.creador} - {self.titulo}"

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='comentarios')
    def __str__(self):
        return f"{self.creador} - {self.tema}"
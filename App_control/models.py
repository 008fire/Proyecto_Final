from django.db import models
from django.contrib.auth.models import User


class Articulos(models.Model):
    
    nombre = models.CharField(max_length=64)
    marca = models.CharField(max_length=64)
    precio = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.marca}, {self.precio}"


class Cliente(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    

class delivery(models.Model):
    nombre = models.CharField(max_length=256) 
    ubicacion = models.CharField(max_length=256)
    habilitado = models.BooleanField(default=False) 
    def __str__(self):
        return f"{self.nombre}"

 
class Publicacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    imagencontenido = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    comentario = models.ForeignKey(Publicacion, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)

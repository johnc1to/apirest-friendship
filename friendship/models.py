from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Incidentes(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    img = models.CharField(max_length=6000)
    latitud = models.DecimalField(max_digits=36, decimal_places=18)
    longitud = models.DecimalField(max_digits=36, decimal_places=18)
    def __str__(self):
        return self.nombre

class Centros(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    img = models.CharField(max_length=6000)
    latitud = models.DecimalField(max_digits=36, decimal_places=18)
    longitud = models.DecimalField(max_digits=36, decimal_places=18)

    def __str__(self):
        return self.nombre


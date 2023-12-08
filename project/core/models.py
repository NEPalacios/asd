from django.db import models


# Create your models here.
class Stock(models.Model):
    producto = models.CharField(max_length=10)
    cantidad = models.IntegerField()
    def __str__(self):
        return f"{self.producto} - ({self.cantidad})"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
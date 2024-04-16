from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} "


class Producto(models.Model):
    nombre_de_producto = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    codigo = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.nombre_de_producto} "
    
class Sucursal(models.Model):
    tipo_de_sucursal = models.CharField(max_length=20)
    tamaño = models.CharField(max_length=20)
    localidad = models.CharField(max_length=20)
    cantidad_de_empleados = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.tipo_de_sucursal} "
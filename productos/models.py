from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from django.conf import settings


class Producto(models.Model):
    precio = models.IntegerField(default=0)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    creacion = models.DateTimeField(auto_now=True)
    actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class ProdcutoImagen(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE,
                                 related_name='images')
    imagen = models.ImageField()

    def __str__(self):
        return self.imagen.url


class LogBuy(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        'productos.Producto',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    def __str__(self):
        return "producto {} comprado".format(self.product)

from __future__ import unicode_literals

from django.db import models
from usuarios.models import Usuario
from productos.models import Producto
from django.conf import settings

class Venta(models.Model):
    total = models.IntegerField(default=0)
    username = models.ForeignKey(Usuario)
    producto = models.ManyToManyField(Producto)

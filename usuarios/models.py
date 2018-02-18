from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Usuario(models.Model):
    username = models.CharField(max_length=50)

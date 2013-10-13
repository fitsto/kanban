from django.db import models

from django.contrib.auth.models import User

class Grupo(models.Model):
	nombre = models.CharField(max_length=150)
	propietario = models.ForeignKey(User)
	fecha_creacion = models.DateTimeField()


class Proyecto(models.Model):
	grupo = models.ForeignKey(Grupo)
	nombre = models.CharField(max_length=150)
	descripcion = models.CharField(max_length=300)
	integrantes = models.ManyToManyField(User)
	fecha_creacion = models.DateTimeField()
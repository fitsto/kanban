from django.db import models

from django.contrib.auth.models import User


class Grupo(models.Model):
	nombre = models.CharField(max_length=150)
	propietario = models.ForeignKey(User)
	fecha_creacion = models.DateTimeField(auto_now_add=True)


class Proyecto(models.Model):
	grupo = models.ForeignKey(Grupo)
	nombre = models.CharField(max_length=150)
	descripcion = models.CharField(max_length=300)
	integrantes = models.ManyToManyField(User)
	fecha_creacion = models.DateTimeField()


class Etapa(models.Model):
	proyecto = models.ForeignKey(Proyecto)
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=300)
	orden = models.IntegerField()


class Categoria(models.Model):
	proyecto = models.ForeignKey(Proyecto)
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=300)
	prioridad = models.IntegerField()
	color = models.CharField(max_length=10)


class Tarea(models.Model):
	ESTIMACION_TIPO_CHOICES = (
		('h','Horas'),
		('d','Dias'),
	)
	proyecto = models.ForeignKey(Proyecto)
	nombre = models.CharField(max_length=100)
	etapa = models.ForeignKey(Etapa)
	estimacionTiempo = models.IntegerField()
	estimacionTipo = models.CharField(max_length=1,choices=ESTIMACION_TIPO_CHOICES,default='h')
	responsable = models.ForeignKey(User)
	fechaInicio = models.DateTimeField()
	fechaFin = models.DateTimeField()
	categoria = models.ForeignKey(Categoria)

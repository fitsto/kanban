from django.test import TestCase
from django.utils import timezone
from principal.models import Grupo, Proyecto, Etapa, Categoria,Tarea

from django.contrib.auth.models import User

class GrupoModelTest(TestCase):

	def test_creando_nuevo_grupo_de_trabajo(self):
		usuario = User.objects.create(username='user1')
		# creamos el grupo
		grupo = Grupo()
		grupo.nombre = "Grupo 1"
		grupo.propietario = usuario
		grupo.fecha_creacion = timezone.now()

		# guardamos
		grupo.save()

		# comprobamos que se guardo correctamente en la bd
		grupos = Grupo.objects.all()

		self.assertEquals(len(grupos),1)
		grupo_db = grupos[0]
		self.assertEquals(grupo_db,grupo)

		#comprobamos que se guardaron correctamente los campos
		self.assertEquals(grupo_db.nombre, "Grupo 1")
		self.assertEquals(grupo_db.propietario, usuario)
		self.assertEquals(grupo_db.fecha_creacion, grupo.fecha_creacion)


class ProyectoModelTest(TestCase):

	def test_creando_un_proyecto_del_grupo(self):
		usuario = User.objects.create(username='user1')
		# partimos creando el grupo
		grupo = Grupo()
		grupo.nombre = "Grupo 1"
		grupo.propietario = usuario
		grupo.fecha_creacion = timezone.now()
		grupo.save()

		proyecto = Proyecto()
		proyecto.grupo = grupo
		proyecto.nombre = "Proyecto 1"
		proyecto.descripcion = "Primer proyecto del grupo"
		proyecto.fecha_creacion = timezone.now()

		proyecto.save()

		proyecto.integrantes.add(usuario)

		proyectos = Proyecto.objects.all()

		# comprobamos que obtenemos el proyecto guardado de la base de datos
		self.assertEquals(len(proyectos),1)
		proyecto_db = proyectos[0]
		self.assertEquals(proyecto_db,proyecto)

		# comprobamos que hay solo un integrante agregado
		self.assertEquals(len(proyecto_db.integrantes.all()),1)

		# comprobamos que se guardaron correctamente los campos
		self.assertEquals(proyecto_db.nombre, "Proyecto 1")
		self.assertEquals(proyecto_db.descripcion, "Primer proyecto del grupo")
		self.assertEquals(proyecto_db.integrantes.all()[0], usuario)
		self.assertEquals(proyecto_db.fecha_creacion, proyecto.fecha_creacion)

class EtapaModelTest(TestCase):

	def test_crear_tres_etapas_de_un_proyecto(self):
		usuario = User.objects.create(username='user1')
		# partimos creando el grupo
		grupo = Grupo()
		grupo.nombre = "Grupo 1"
		grupo.propietario = usuario
		grupo.fecha_creacion = timezone.now()
		grupo.save()

		proyecto = Proyecto()
		proyecto.grupo = grupo
		proyecto.nombre = "Proyecto 1"
		proyecto.descripcion = "Primer proyecto del grupo"
		proyecto.fecha_creacion = timezone.now()

		proyecto.save()

		proyecto.integrantes.add(usuario)

		# creamos la primera etapa
		etapa1 = Etapa()
		etapa1.proyecto = proyecto
		etapa1.nombre = "Pendientes"
		etapa1.descripcion = "En esta etapa se encontrararan todas las tareas pendientes"
		etapa1.orden = 1

		# guardamos la etapa1
		etapa1.save()

		# obtenemos todas las etapas de la base
		etapas = Etapa.objects.all()

		# comprobamos que este solamente la etapa que guardamos
		self.assertEquals(len(etapas),1)

		# obtenemos la etapa 1 de la bd
		etapa1_db = etapas[0]

		# comprobamos que sea igual a la etapa que definimos
		self.assertEquals(etapa1_db,etapa1)

		#comprobamos que se guardaron los campos correctamente
		self.assertEquals(etapa1_db.nombre, "Pendientes")
		self.assertEquals(etapa1_db.descripcion, "En esta etapa se encontrararan todas las tareas pendientes")
		self.assertEquals(etapa1_db.orden, 1)

		# creamos una segunda etapa
		etapa2 = Etapa()
		etapa2.proyecto = proyecto
		etapa2.nombre = "En Curso"
		etapa2.descripcion = "En esta etapa se encontraran todas las tareas que estan en curso"
		etapa2.orden = 2

		# guardamos la etapa2
		etapa2.save()

		# obtenemos todas las etapas de la base
		etapas = Etapa.objects.all()

		# comprobamos que se encuentren las dos etapas que hemos creado
		self.assertEquals(len(etapas),2)

		# obtenemos la etapa2 de la bd
		etapa2_db = etapas[1]

		# comprobamos que sea igual a la etapa que definimos
		self.assertEquals(etapa2_db,etapa2)

		# creamos una tercera etapa, pero esta vez sin descripcion 
		# para que sea opcional este campo
		etapa3 = Etapa()
		etapa3.proyecto = proyecto
		etapa3.nombre = "Finalizadas"
		etapa3.orden = 3

		# guardamos la etapa 3
		etapa3.save()

		# obtenemos todas las etapas de la base
		etapas = Etapa.objects.all()

		# comprobamos que se encuentren las 3 etapas que hemos creado
		self.assertEquals(len(etapas),3)

		#obtenemos la etapa3 de la bd
		etapa3_db = etapas[2]

		# comprobamos que sea igual a la etapa que definimos
		self.assertEquals(etapa3_db,etapa3)

class CategoriaModelTest(TestCase):

	def test_crear_una_categoria_del_proyecto(self):
		usuario = User.objects.create(username='user1')
		# partimos creando el grupo
		grupo = Grupo()
		grupo.nombre = "Grupo 1"
		grupo.propietario = usuario
		grupo.fecha_creacion = timezone.now()
		grupo.save()

		proyecto = Proyecto()
		proyecto.grupo = grupo
		proyecto.nombre = "Proyecto 1"
		proyecto.descripcion = "Primer proyecto del grupo"
		proyecto.fecha_creacion = timezone.now()

		proyecto.save()

		proyecto.integrantes.add(usuario)

		#creamos la categoria
		categoria = Categoria()
		categoria.proyecto = proyecto
		categoria.nombre = "Bug"
		categoria.descripcion = "Error del sistema"
		categoria.prioridad = 1
		categoria.color = "red"

		# guardamos la categoria
		categoria.save()

		# obtenemos las categorias de la base
		categorias = Categoria.objects.all()

		# comprobamos que este la categoria que guardamos en la base
		self.assertEquals(len(categorias),1)

		# 0btenemos la categoria de la base
		categoria_db = categorias[0]

		# comprobamos que la categoria de la bd sea igual a la categoria que definimos
		self.assertEquals(categoria_db,categoria)

		# comprobamos que guardamos los campos correctamente
		self.assertEquals(categoria_db.nombre,"Bug")
		self.assertEquals(categoria_db.descripcion,"Error del sistema")
		self.assertEquals(categoria_db.prioridad,1)
		self.assertEquals(categoria_db.color,"red")


class TareaModelTest(TestCase):

	def test_crear_una_tarea_del_proyecto(self):
		usuario = User.objects.create(username='user1')
		# partimos creando el grupo
		grupo = Grupo()
		grupo.nombre = "Grupo 1"
		grupo.propietario = usuario
		grupo.fecha_creacion = timezone.now()
		grupo.save()

		proyecto = Proyecto()
		proyecto.grupo = grupo
		proyecto.nombre = "Proyecto 1"
		proyecto.descripcion = "Primer proyecto del grupo"
		proyecto.fecha_creacion = timezone.now()

		proyecto.save()

		proyecto.integrantes.add(usuario)

		#creamos la categoria
		categoria = Categoria()
		categoria.proyecto = proyecto
		categoria.nombre = "Bug"
		categoria.descripcion = "Error del sistema"
		categoria.prioridad = 1
		categoria.color = "red"

		# guardamos la categoria
		categoria.save()

		# creamos la primera etapa
		etapa = Etapa()
		etapa.proyecto = proyecto
		etapa.nombre = "Pendientes"
		etapa.descripcion = "En esta etapa se encontrararan todas las tareas pendientes"
		etapa.orden = 1

		# guardamos la etapa
		etapa.save()

		# creamos la tarea
		tarea = Tarea()
		tarea.proyecto = proyecto
		tarea.nombre = "Tarea 1"
		tarea.etapa = etapa
		tarea.estimacionTiempo = 3
		tarea.estimacionTipo = "h"
		tarea.responsable = usuario
		tarea.fechaInicio = timezone.now()
		tarea.fechaFin = timezone.now()
		tarea.categoria = categoria

		tarea.save()

		# obtenemos las tareas
		tareas = Tarea.objects.all()

		# comprobamos que este la tarea que guardamos
		self.assertEquals(len(tareas),1)

		# obtenemos la tarea de la base
		tarea_db = tareas[0]

		# comprobamos que la tarea de la base de datos sea igual
		# a la tarea que definimos
		self.assertEquals(tarea_db,tarea)

		# comprobamos que los campos se guardaron correctamente
		self.assertEquals(tarea_db.proyecto,proyecto)
		self.assertEquals(tarea_db.nombre,"Tarea 1")
		self.assertEquals(tarea_db.etapa,etapa)
		self.assertEquals(tarea_db.estimacionTiempo,3)
		self.assertEquals(tarea_db.estimacionTipo,"h")
		self.assertEquals(tarea_db.responsable,usuario)
		self.assertEquals(tarea_db.fechaInicio,tarea.fechaInicio)
		self.assertEquals(tarea_db.fechaFin,tarea.fechaFin)
		self.assertEquals(tarea_db.categoria,categoria)
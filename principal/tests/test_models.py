from django.test import TestCase
from django.utils import timezone
from principal.models import Grupo, Proyecto, Etapa, Categoria

from django.contrib.auth.models import User

class GrupoModelTest(TestCase):
	def setUp(self):
		self.u1 = User.objects.create(username='user1')

	def tearDown(self):
		self.u1.delete()

	def test_creando_nuevo_grupo_de_trabajo(self):
		# creamos el grupo
		grupo = Grupo()
		grupo.nombre = "Grupo 1"
		grupo.propietario = self.u1
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
		self.assertEquals(grupo_db.propietario, self.u1)
		#self.assertEquals(grupo_db.integrantes.all()[0], self.u1)
		self.assertEquals(grupo_db.fecha_creacion, grupo.fecha_creacion)


class ProyectoModelTest(TestCase):
	def setUp(self):
		self.u1 = User.objects.create(username='user1')

	def tearDown(self):
		self.u1.delete()

	def test_creando_un_proyecto_del_grupo(self):
		# partimos creando el grupo
		grupo = Grupo()
		grupo.nombre = "Grupo 1"
		grupo.propietario = self.u1
		grupo.fecha_creacion = timezone.now()
		grupo.save()

		proyecto = Proyecto()
		proyecto.grupo = grupo
		proyecto.nombre = "Proyecto 1"
		proyecto.descripcion = "Primer proyecto del grupo"
		proyecto.fecha_creacion = timezone.now()

		proyecto.save()

		proyecto.integrantes.add(self.u1)

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
		self.assertEquals(proyecto_db.integrantes.all()[0], self.u1)
		self.assertEquals(proyecto_db.fecha_creacion, proyecto.fecha_creacion)

class EtapaModelTest(TestCase):
	def setUp(self):
		self.u1 = User.objects.create(username='user1')

	def tearDown(self):
		self.u1.delete()

	def test_crear_tres_etapas_de_un_proyecto(self):
		# partimos creando el grupo
		grupo = Grupo()
		grupo.nombre = "Grupo 1"
		grupo.propietario = self.u1
		grupo.fecha_creacion = timezone.now()
		grupo.save()

		proyecto = Proyecto()
		proyecto.grupo = grupo
		proyecto.nombre = "Proyecto 1"
		proyecto.descripcion = "Primer proyecto del grupo"
		proyecto.fecha_creacion = timezone.now()

		proyecto.save()

		proyecto.integrantes.add(self.u1)

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
	def setUp(self):
		self.u1 = User.objects.create(username='user1')

	def tearDown(self):
		self.u1.delete()

	def test_crear_una_categoria_del_proyecto(self):
		# partimos creando el grupo
		grupo = Grupo()
		grupo.nombre = "Grupo 1"
		grupo.propietario = self.u1
		grupo.fecha_creacion = timezone.now()
		grupo.save()

		proyecto = Proyecto()
		proyecto.grupo = grupo
		proyecto.nombre = "Proyecto 1"
		proyecto.descripcion = "Primer proyecto del grupo"
		proyecto.fecha_creacion = timezone.now()

		proyecto.save()

		proyecto.integrantes.add(self.u1)

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
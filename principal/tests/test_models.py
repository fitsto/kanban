from django.test import TestCase
from django.utils import timezone
from principal.models import Grupo, Proyecto

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

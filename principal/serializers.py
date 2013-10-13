from rest_framework import serializers

from .models import Grupo,Proyecto,Etapa,Categoria,Tarea
from django.contrib.auth.models import User

class GrupoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Grupo
		fields = ('url', 'nombre','propietario','fecha_creacion',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username','email')
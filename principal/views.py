# Create your views here.
from .serializers import GrupoSerializer, UserSerializer
from rest_framework import viewsets

from .models import Grupo

from django.contrib.auth.models import User

class GrupoViewSet(viewsets.ModelViewSet):
	queryset = Grupo.objects.all()
	serializer_class = GrupoSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

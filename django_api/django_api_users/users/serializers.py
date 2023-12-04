# Definimos el modelo y los campos para la API
from rest_framework import routers,serializers,viewsets
from .models import User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'lastname', 'email', 'created_at']
from rest_framework import serializers
from .models import PocionWiki

# Creando el serializer para la construcción de la API
class PocionWikiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PocionWiki
        fields = ('id', 'nombre', 'ingredientes') 
        
        
        
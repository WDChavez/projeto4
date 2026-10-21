from rest_framework import serializers  # ferramentas do DRF transformar a tabela em JSON
from .models import Generos, Filmes        # modelos usados pelos serializers

class GenerosSerializer(serializers.ModelSerializer):
   class Meta:
       model = Generos
       fields = '__all__' 

class FilmesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Filmes
       fields = '__all__' 

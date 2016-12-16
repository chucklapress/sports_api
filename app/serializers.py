from rest_framework import serializers
from app.models import Player

class PlayerSerializer(serializers.ModelSerializer):



    class Meta:
        model = Player
        fields = ('id','name', 'weight','position','birth_year')

        

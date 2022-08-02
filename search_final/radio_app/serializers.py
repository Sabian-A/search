
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import PlayerRadiostation, PlayerRadiostation
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerRadiostation
        fields = '__all__'

class FavouritesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =PlayerRadiostation
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PlayerRadiostation.objects.all(),
                fields=['station_id', 'user_id']
            )
        ]
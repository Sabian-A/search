from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import PlayerPodcasthost, PlayerPodcastseason, PlayerPodcastcategory, PlayerPodcastepisode, PlayerPodcastplaylist, PlayerPodcastplaylistepisodes, PlayerPodcastfavourites

class FavouritesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlayerPodcastfavourites
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PlayerPodcastfavourites.objects.all(),
                fields=['episode_id', 'user_id']
            )
        ]

class PlayListEpisodesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerPodcastplaylistepisodes
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PlayerPodcastplaylistepisodes.objects.all(),
                fields=['playlist_id', 'episode_id']
            )
        ]

class PlayListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlayerPodcastplaylist
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PlayerPodcastplaylist.objects.all(),
                fields=['playlist_name', 'user_id']
            )
        ]

class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerPodcastepisode
        fields = '__all__'

class PodcastCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerPodcastcategory
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerPodcastseason
        fields = '__all__'

class HostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlayerPodcasthost
        fields = '__all__'
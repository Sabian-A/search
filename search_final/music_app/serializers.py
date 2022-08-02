from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import  PlayerMusicalbum,  PlayerMusicartist,  PlayerMusictrack,  PlayerMusicgenre,  PlayerMusiclyrics,  PlayerMusicplaylist, PlayerMusicplaylisttracks,  PlayerMusicfavourites

class FavouritesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  PlayerMusicfavourites
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset= PlayerMusicfavourites.objects.all(),
                fields=['track_id', 'user_id']
            )
        ]

class PlayListTracksSerializer(serializers.ModelSerializer):

    class Meta:
        model =  PlayerMusicplaylisttracks
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset= PlayerMusicplaylisttracks.objects.all(),
                fields=['playlist_id', 'track_id']
            )
        ]

class PlayListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  PlayerMusicplaylist
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset= PlayerMusicplaylist.objects.all(),
                fields=['playlist_name', 'user_id']
            )
        ]



class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model =  PlayerMusicgenre
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  PlayerMusicartist
        fields = '__all__'
class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer

    class Meta:
        model =  PlayerMusicalbum
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    album = AlbumSerializer
    artist = ArtistSerializer
    gener = GenreSerializer

    class Meta:
        model =  PlayerMusictrack
        fields = [
            "id",
            "track_name",
            "track_file",
            "track_description",
            "track_release_date",
            "album",
            "artist",
            "gener"
        ]
class LyricsSerializer(serializers.ModelSerializer):
    track = TrackSerializer
    class Meta:
        model =  PlayerMusiclyrics
        fields = '__all__'

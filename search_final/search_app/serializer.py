import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from music_app.documents import PlayerMusictrackDocument, PlayerMusicartistDocument, PlayerMusicalbumDocument, PlayerMusicgenreDocument, PlayerMusiclyricsDocument
from radio_app.documents import PlayerRadiostationDocument
from podcast_app.documents import PlayerPodcastcategoryDocument, PlayerPodcastepisodeDocument,  PlayerPodcasthostDocument, PlayerPodcastseasonDocument

__all__ = (
    'PlayerMusictrackDocumentSerializer',
    'PlayerMusicartistDocumentSerializer',
    'PlayerMusicalbumDocumentSerializer',
    'PlayerMusicgenreDocumentSerializer',
    'PlayerRadiostationDocumentSerializer',
    'PlayerPodcastcategoryDocumentSerializer',
    'PlayerPodcastepisodeDocumentSerializer',
    'PlayerPodcasthostDocumentSerializer',
    'PlayerPodcastseasonDocumentSerializer',

)
class PlayerMusictrackDocumentSerializer(DocumentSerializer):
    """Serializer for the PlayerMusictrack document."""

    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = PlayerMusictrackDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'track_name',
            'track_description',
            'track_file',
            'track_release_date',
            'album_id',
            'artist_id',
            'genre_id',
        )
        
        
        
class PlayerMusicartistDocumentSerializer(DocumentSerializer):
    """Serializer for the PlayerMusicartist document."""
    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = PlayerMusicartistDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields =(
            'id',
            'artist_name',
            'artist_title',
            'artist_description',
            'artist_cover',
            'created_at',
            'updated_at',
        )
        

class PlayerMusicalbumDocumentSerializer(DocumentSerializer):
    """Serializer for the PlayerMusicalbum document."""
    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = PlayerMusicalbumDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'album_title',
            'album_description',
            'album_cover',
            'artist_id',
            'created_at',
            'updated_at',
        )
        

class PlayerMusicgenreDocumentSerializer(DocumentSerializer):
    """Serializer for the PlayerMusicgenre document."""
    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = PlayerMusicgenreDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'genre_title',
            'genre_description',
            'genre_cover',
            'created_at',
            'updated_at',
        )
        

class PlayerMusiclyricsDocumentSerializer(DocumentSerializer):
    """Serializer for the PlayerMusiclyrics document."""
    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = PlayerMusiclyricsDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'lyrics_title',
            'track_id',
            'lyrics_detail',
            'created_at',
            'updated_at',
        )


#########################################################


class PlayerRadiostationDocumentSerializer(DocumentSerializer):
    """Serializer for the PlayerRadiostation document."""
    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = PlayerRadiostationDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'station_name',
            'station_frequency',
            'station_url',
            'station_cover',
            'station_description',
            'created_at',
            'updated_at',
        )
        

#########################################################


class PlayerPodcastcategoryDocumentSerializer(DocumentSerializer):
    """Serializer for the PlayerPodcastcategory document."""
    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = PlayerPodcastcategoryDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'Podcast_category_title',
            'Podcast_category_description',
            'Podcast_category_cover',
            'created_at',
            'updated_at',
        )
        


class PlayerPodcastepisodeDocumentSerializer(DocumentSerializer):
    """Serializer for the PlayerPodcastepisode document."""

    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = PlayerPodcastepisodeDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'episode_title',
            'episode_description',
            'episode_file',
            'episode_release_date',
            'season_id',
            'host_id',
            'podcast_category_id',
            'created_at',
            'updated_at',
        )
        


class PlayerPodcasthostDocumentSerializer(DocumentSerializer):
    """Serializer for the PlayerPodcasthost document."""
    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = PlayerPodcasthostDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'host_name',
            'host_title',
            'host_description',
            'host_cover',
            'created_at',
            'updated_at',
        )
        
        


class PlayerPodcastseasonDocumentSerializer(DocumentSerializer):
    """Serializer for the PlayerPodcastseason document."""
    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = PlayerPodcastseasonDocument
        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'season_title',
            'season_description',
            'season_cover',
            'host_id',
            'created_at',
            'updated_at',
        )
        
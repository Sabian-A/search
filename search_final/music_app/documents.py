from django_elasticsearch_dsl import Document, fields

from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer
from music_app.models import PlayerMusicalbum, PlayerMusicartist,PlayerMusicgenre, PlayerMusiclyrics, PlayerMusictrack
#from radio_app.models import PlayerRadiostation, PlayerRadiostationfavourites
#from podcast_app.models import PlayerPodcastcategory, PlayerPodcastepisode, PlayerPodcastfavourites, PlayerPodcasthost, PlayerPodcastplaylist, PlayerPodcastplaylistepisodes, PlayerPodcastseason

html_strip = analyzer(
    'html_strip',
    tokenizer="edge_ngram",
    filter=[ "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)
@registry.register_document
class PlayerMusictrackDocument(Document):

    album = fields.ObjectField(
        properties={
        "id": fields.IntegerField(),
        "album_title": fields.TextField(), 
        "album_description":fields.TextField(),
        },
        
    )
    artist = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "artist_name": fields.TextField(), 
        "artist_title": fields.TextField(),
        "artist_description":fields.TextField(),},

    )
    gener = fields.ObjectField(properties={"genre_title": fields.TextField(),"genre_description": fields.TextField()
    },
    
    
    )
    
    
    

    class Index:
        name = "music"

    class Django:
        model = PlayerMusictrack

        fields = [
            "id",
            "track_name",
            "track_file",
            "track_description",
            "track_release_date",
        ]
    


@registry.register_document
class PlayerMusicartistDocument(Document):
    class Index:
        name = "music"

    class Django:
        model = PlayerMusicartist

        fields = [
            "id",
            "artist_name",
            "artist_title",
            "artist_cover",
            "artist_description",
            
        ]


@registry.register_document
class PlayerMusicalbumDocument(Document):

    artist = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "artist_name": fields.TextField(), 
        "artist_title": fields.TextField(),
        "artist_description":fields.TextField(),}, 
        analyzer=html_strip,
        fields={
            'raw': fields.TextField
            (analyzer='keyword'),
        }
        )


    class Index:
        name = "music"

    class Django:
        model = PlayerMusicalbum
        fields = [
            "id",
            "album_title",
            "album_cover",
            "album_description",  
        ]


@registry.register_document
class PlayerMusicgenreDocument(Document):

    class Index:
        name = "music"

    class Django:
        model = PlayerMusicgenre

        fields = [
            "id",
            "genre_title",
            "genre_cover",
            "genre_description",
            
        ]
        
@registry.register_document
class PlayerMusiclyricsDocument(Document):

    class Index:
        name = "music"

    class Django:
        model = PlayerMusiclyrics

        fields = [
            "id",
            "lyrics_title",
            "lyrics_detail",
            
            
        ]

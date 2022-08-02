from django_elasticsearch_dsl import Document, fields
from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl.registries import registry

#from music_app.models import PlayerMusicalbum, PlayerMusicartist, PlayerMusicfavourites, PlayerMusicgenre, PlayerMusiclyrics, PlayerMusicplaylist, PlayerMusictrack
#from radio_app.models import PlayerRadiostation, PlayerRadiostationfavourites
from podcast_app.models import PlayerPodcastcategory, PlayerPodcastepisode,PlayerPodcasthost, PlayerPodcastseason

html_strip = analyzer(
    'html_strip',
    tokenizer="edge_ngram",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@registry.register_document
class PlayerPodcastepisodeDocument(Document):

    season = fields.ObjectField(
        properties={
        "id": fields.IntegerField(),
        "season_title": fields.TextField(), 
        "season_description":fields.TextField(),
        "season_cover": fields.TextField(),
        },
        
    )
    host = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "host_name": fields.TextField(), 
        "host_title": fields.TextField(),
        "host_cover": fields.TextField(),
        "host_description":fields.TextField(),},
        
    
    )
    podcast_catagory = fields.ObjectField(properties={
    "id": fields.IntegerField(),    
    "podcast_catagory_title": fields.TextField(),
    "podcast_catagory_description": fields.TextField(),
    "podcast_catagory_cover": fields.TextField(),
    },
    
    )
    
    
    

    class Index:
        name = "podcast"

    class Django:
        model = PlayerPodcastepisode

        fields = [
            "id",
            "episode_title",
            "episode_file",
            "episode_description",
            "episode_release_date",
        ]
    


@registry.register_document
class PlayerPodcasthostDocument(Document):

    class Index:
        name = "podcast"

    class Django:
        model = PlayerPodcasthost

        fields = [
            "id",
            "host_name",
            "host_title",
            "host_cover",
            "host_description",
            
        ]


@registry.register_document
class PlayerPodcastseasonDocument(Document):

    host = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "host_name": fields.TextField(), 
        "host_title": fields.TextField(),
        "host_description":fields.TextField(),},
        
        )
    
    
    

    class Index:
        name = "podcast"

    class Django:
        model = PlayerPodcastseason
        fields = [
            "id",
            "season_title",
            "season_cover",
            "season_description",  
        ]


@registry.register_document
class PlayerPodcastcategoryDocument(Document):

    class Index:
        name = "podcast"

    class Django:
        model = PlayerPodcastcategory

        fields = [
            "id",
            "podcast_category_title",
            "podcast_category_cover",
            "podcast_category_description",
            
        ]

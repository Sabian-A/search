from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer
#from music_app.models import PlayerMusicalbum, PlayerMusicartist, PlayerMusicfavourites, PlayerMusicgenre, PlayerMusiclyrics, PlayerMusicplaylist, PlayerMusictrack
from radio_app.models import PlayerRadiostation
#from podcast_app.models import PlayerPodcastcategory, PlayerPodcastepisode, PlayerPodcastfavourites, PlayerPodcasthost, PlayerPodcastplaylist, PlayerPodcastplaylistepisodes, PlayerPodcastseason

html_strip = analyzer(
    'html_strip',
    tokenizer="edge_ngram",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)
@registry.register_document
class PlayerRadiostationDocument(Document):

    class Index:
        name = "radio"

    class Django:
        model = PlayerRadiostation

        fields = [
            "id",
            "station_name",
            "station_frequency",
            "station_description",
            "station_cover",
            "station_url",
        ]
    

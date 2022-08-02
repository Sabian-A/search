from django.shortcuts import render
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_QUERY_EXCLUDE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

#########################################################

from music_app.documents import PlayerMusictrackDocument, PlayerMusicartistDocument, PlayerMusicalbumDocument, PlayerMusicgenreDocument, PlayerMusiclyricsDocument
from radio_app.documents import PlayerRadiostationDocument
from podcast_app.documents import PlayerPodcastcategoryDocument, PlayerPodcastepisodeDocument,  PlayerPodcasthostDocument, PlayerPodcastseasonDocument

#########################################################

from  .serializer import PlayerMusictrackDocumentSerializer, PlayerMusicartistDocumentSerializer,  PlayerMusicalbumDocumentSerializer, PlayerMusicgenreDocumentSerializer, PlayerMusiclyricsDocumentSerializer, PlayerRadiostationDocumentSerializer, PlayerPodcastcategoryDocumentSerializer, PlayerPodcastepisodeDocumentSerializer, PlayerPodcasthostDocumentSerializer, PlayerPodcastseasonDocumentSerializer

# Create your views here.


class PlayerMusictrackDocumentView(BaseDocumentViewSet):
    """The PlayerMusictrackDocument view."""

    document = PlayerMusictrackDocument
    serializer_class = PlayerMusictrackDocumentSerializer, 
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        'track_name',
        'track_description',
    )
    
    
    # Define filter fields
    filter_fields = {
        'id': {
            'field': 'id',
            # Note, that we limit the lookups of id field in this example,
            # to `range`, `in`, `gt`, `gte`, `lt` and `lte` filters.
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'track_name': 'track_name',
        'track_description': 'track_description',
        'track_release_date': 'track_release_date',
        
        
    }
    
    
    
    #Define ordering fields
    ordering_fields = {
        'id': 'id',
        'track_name': 'track_name',
        'track_description': 'track_description',
        'track_release_date': 'track_release_date',
    }
    # Specify default ordering
    ordering = ('id', 'track_name', 'track_description', 'track_release_date',)
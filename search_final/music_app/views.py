
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.http import HttpResponse
from .models import  PlayerMusicalbum,  PlayerMusicartist,  PlayerMusictrack,  PlayerMusicgenre,  PlayerMusiclyrics,  PlayerMusicplaylist, PlayerMusicplaylisttracks,  PlayerMusicfavourites
from .serializers import ArtistSerializer, AlbumSerializer, GenreSerializer, TrackSerializer, LyricsSerializer, FavouritesSerializer, PlayListSerializer, PlayListTracksSerializer


from rest_framework import permissions
from rest_framework.decorators import APIView, permission_classes



# Pagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

# Create your views here.

class ArtistViewSet(viewsets.ModelViewSet):
    
    queryset = PlayerMusicartist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = StandardResultsSetPagination

class AlbumViewSet(viewsets.ModelViewSet):
    
    queryset = PlayerMusicalbum.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = StandardResultsSetPagination

class GenreViewSet(viewsets.ModelViewSet):
    
    queryset = PlayerMusicgenre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = StandardResultsSetPagination

class TrackViewSet(viewsets.ModelViewSet):
    
    queryset = PlayerMusictrack.objects.all()
    serializer_class = TrackSerializer
    pagination_class = StandardResultsSetPagination


class LyricsViewSet(viewsets.ModelViewSet):
    
    queryset = PlayerMusiclyrics.objects.all()
    serializer_class = LyricsSerializer
    pagination_class = StandardResultsSetPagination

class PlayListViewSet(viewsets.ModelViewSet):
    
    queryset = PlayerMusicplaylist.objects.all()
    serializer_class = PlayListSerializer
    pagination_class = StandardResultsSetPagination

class PlayListTracksViewSet(viewsets.ModelViewSet):
    
    queryset = PlayerMusicplaylisttracks.objects.all()
    serializer_class = PlayListTracksSerializer
    pagination_class = StandardResultsSetPagination

class FavouritesViewSet(viewsets.ModelViewSet):

    queryset = PlayerMusicfavourites.objects.all()
    serializer_class = FavouritesSerializer
    pagination_class = StandardResultsSetPagination
    
    
from .documents import PlayerMusictrackDocument, PlayerMusicartistDocument, PlayerMusicalbumDocument, PlayerMusicgenreDocument, PlayerMusiclyricsDocument
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from django.http import HttpResponse
from elasticsearch_dsl import Q


class SearchPlayerMusictrack(APIView, LimitOffsetPagination):
    TrackSerializer = TrackSerializer
    search_document = PlayerMusictrackDocument

    def get(self, request, query):
        try:
            q = Q(
                'multi_match',
                query=query,
                fields=[
                    'PlayerMusicalbum.album_title',
                    'PlayerMusicartist.artist_name']
                , fuzziness='auto') & Q(
                    'bool',
                    #     should=[
                    #     Q('match', is_default=True
                    #     ),
                    # ],
                    minimum_should_match=1
                )

            search = self.search_document.search().query(q)
            response = search.execute()

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.TrackSerializer(results, many=True)
            print (serializer.data)
            return self.get_paginated_response(serializer.data)
        

        except Exception as e:
            return HttpResponse(e, status=500)
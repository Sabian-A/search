from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from .views import PlayerMusictrackDocumentView

router = DefaultRouter()
tracks = router.register(r'tracks',
    PlayerMusictrackDocumentView,
    basename ='playermusictrackdocument')

urlpatterns = [
    re_path(r'^', include(router.urls)),
]

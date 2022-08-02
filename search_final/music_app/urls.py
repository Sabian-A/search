from django.urls import include, path
from rest_framework import routers
from .views import SearchPlayerMusictrack

from . import views

router = routers.DefaultRouter()
router.register(
    r"gener/(?P<slug>[^/.]+)",
    views.GenreViewSet,
    basename="PlayerMusicgenre",
)
# router.register(r"item/(?P<id>[^/.]+)", views.SingleProductViewSet, basename="items")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path('search/<str:query>/', SearchPlayerMusictrack.as_view())
]
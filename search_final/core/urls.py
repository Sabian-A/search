# """core URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path,include, re_path

# from music_app import urls as music_app_urls
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]



# urlpatterns = [
#     # ...
#     # Search URLs
#     re_path(r'^search/', include(music_app_urls)),
#     # ...
# ]

from django.urls import include, path
from rest_framework import routers
from music_app.views import SearchPlayerMusictrack

from music_app import views

router = routers.DefaultRouter()

# router.register(r"item/(?P<id>[^/.]+)", views.SingleProductViewSet, basename="items")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path('search/<str:query>/', SearchPlayerMusictrack.as_view())
]
from django.urls import include, path
from rest_framework import routers


from cinema.views import (
    ActorViewSet,
    CinemaHallViewSet,
    GenreHallViewSet,
    MovieViewSet,
)


router = routers.DefaultRouter()
router.register(r"cinema-halls", CinemaHallViewSet, basename="cinemahall")
router.register(r"genres", GenreHallViewSet, basename="genre")
router.register(r"actors", ActorViewSet, basename="actor")
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"movie-sessions", MovieViewSet, basename="moviesession")


urlpatterns = [path("", include(router.urls))]


app_name = "cinema"

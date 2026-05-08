from django.urls import include, path
from rest_framework import routers


from cinema.views import CinemaHallViewSet, GenreHallViewSet


router = routers.DefaultRouter()
router.register(r"cinema-halls", CinemaHallViewSet, basename="cinemahall")
router.register(r"genres", GenreHallViewSet, basename="genre")


urlpatterns = [path("", include(router.urls))]


app_name = "cinema"

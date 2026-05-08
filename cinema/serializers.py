from rest_framework import serializers


from cinema.models import CinemaHall, Genre


class CinemaHallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"
        extra_kwargs = {"url": {"view_name": "cinema:cinemahall-detail"}}


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
        extra_kwargs = {"url": {"view_name": "cinema:genre-detail"}}

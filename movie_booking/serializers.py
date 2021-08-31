from rest_framework.serializers import ModelSerializer
from . import models
from rest_framework import serializers


class MovieSerializer(ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "__all__"


class CitySerializer(ModelSerializer):
    class Meta:
        model = models.City
        fields = "__all__"


class ShowSerializer(ModelSerializer):
    class Meta:
        model = models.Show
        fields = "__all__"


class CinemaHallSerializer(ModelSerializer):
    shows = ShowSerializer(many=True, read_only=True)

    class Meta:
        model = models.CinemaHall
        fields = ["id", "name", "total_seats", "shows"]


class CinemaSerializer(ModelSerializer):
    depth = 2
    cinema_halls = CinemaHallSerializer(many=True)

    class Meta:
        model = models.Cinema
        fields = ["id", "name", "city", "cinema_halls"]


class SeatSerializer(ModelSerializer):
    class Meta:
        model = models.CinemaHall
        fields = "__all__"


class CinemaSeatSerializer(ModelSerializer):
    class Meta:
        model = models.CinemaSeat
        fields = "__all__"


# class ShowSerializer(ModelSerializer):
#     class Meta:
#         model = models.Show
#         fields = "__all__"


class BookingSerializer(ModelSerializer):
    class Meta:
        model = models.Booking
        fields = "__all__"


class ShowSeatSerializer(ModelSerializer):
    class Meta:
        model = models.ShowSeat
        fields = "__all__"


# Create your views here.
from django.db import transaction
from django.db.models import Count
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class CityViewSet(ModelViewSet):
    serializer_class = serializers.CitySerializer

    def get_queryset(self):
        return models.City.objects.all()


class MovieViewSet(ModelViewSet):
    serializer_class = serializers.MovieSerializer

    def get_queryset(self):
        return models.Movie.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = queryset_ = self.filter_queryset(self.get_queryset())
        city = request.GET.get('city')
        if city is not None:
            queryset = queryset_.filter(shows__cinema_hall__cinema__city__name=city)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CinemaViewSet(ModelViewSet):
    serializer_class = serializers.CinemaSerializer

    def get_queryset(self):
        return models.Cinema.objects.all()


class ShowViewSet(ModelViewSet):
    serializer_class = serializers.ShowSerializer

    def get_queryset(self):
        return models.Show.objects.all()

    def retrieve(self, request, *args, **kwargs):
        queryset = queryset_ = self.get_object()
        show_seats = request.GET.get('show_seats')
        if show_seats is not None:
            show_seats_to_check = models.ShowSeat.objects.values("cinema_seat__id").filter(show=queryset_)
            cinema_seats = models.CinemaSeat.objects.filter(cinema_hall__shows=queryset).exclude(id__in=show_seats_to_check)
            cinema_seats_data = serializers.CinemaSeatSerializer(cinema_seats, many=True)
            data = {"total_seats": queryset.cinema_hall.total_seats, "seats_available_count":  cinema_seats.count(), "seats_available": cinema_seats_data.data}
            return Response(data)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)


class BookingViewSet(ModelViewSet):
    serializer_class = serializers.CinemaSerializer

    def get_queryset(self):
        return models.Cinema.objects.all()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        data = request.data
        number_of_seats = data.get('number_of_seats', 0)
        show = data.get('show', '')





# Create your views here.
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


class BookingViewSet(ModelViewSet):
    serializer_class = serializers.CinemaSerializer

    def get_queryset(self):
        return models.Cinema.objects.all()
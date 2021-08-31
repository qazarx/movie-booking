
# Create your views here.
from django.db import transaction
from django.db.models import Count
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
import logging

logger = logging.getLogger(__name__)


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
    serializer_class = serializers.BookingSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Booking.objects.all()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        data = request.data
        cinema_seats = data.get('cinema_seats', [])
        user = request.user
        show = data.get('show', '')

        if len(cinema_seats) > 0:

            booking_data = {"number_of_seats": len(cinema_seats), "status": "B", "show": show, "user": user.id}
            serializer = self.serializer_class(data=booking_data)
            serializer.is_valid(raise_exception=True)
            booking = serializer.save()
            print(booking)
            show_seat_result = []
            for i in cinema_seats:
                show_seats_data = {"status": "B", "cinema_seat": int(i), "show": show, "booking": booking.id}
                show_serializer = serializers.ShowSeatSerializer(data=show_seats_data)
                show_serializer.is_valid(raise_exception=True)
                show_seat = show_serializer.save()
                data = serializers.ShowSeatSerializer(show_seat).data
                show_seat_result.append(data)
            return Response({"message": "TICKETS BOOKED", "tickets": show_seat_result})
        else:
            logger.error("Error in cinema creation")
            return Response({"message": "some problem occurred, please check cinema id and show id"}, status=status.HTTP_400_BAD_REQUEST)




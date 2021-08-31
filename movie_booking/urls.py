from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'movie_booking'

router = DefaultRouter()
router.register(r'city', CityViewSet, basename='city')
router.register(r'movie', MovieViewSet, basename='movie')
router.register(r'cinema', CinemaViewSet, basename='cinema')
router.register(r'shows', ShowViewSet, basename='shows')
router.register(r'booking', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]
from django.contrib import admin

# Register your models here.
from movie_booking.models import *


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


@admin.register(CinemaSeat)
class SeatAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


@admin.register(Booking)
class ShowAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


@admin.register(ShowSeat)
class ShowAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
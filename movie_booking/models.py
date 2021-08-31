from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    duration = models.DurationField()
    language = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Cinema(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='cinemas', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    total_seats = models.IntegerField(default=0)
    cinema = models.ForeignKey(Cinema, related_name='cinema_halls', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CinemaSeat(models.Model):
    class TypeChoices(models.TextChoices):
        A = 'A'
        B = 'B'
        C = 'C'
        D = 'D'
        E = 'E'
        F = 'F'
        G = 'G'
    seat_number = models.IntegerField()
    type = models.CharField(choices=TypeChoices.choices, max_length=10, default=TypeChoices.A)
    cinema_hall = models.ForeignKey(CinemaHall, related_name="seats", on_delete=models.CASCADE)

    def __str__(self):
        return "Seats " + str(self.seat_number) + self.type + " for " + str(self.cinema_hall) + " at " + str(self.cinema_hall.cinema)


class Show(models.Model):
    class StatusChoices(models.TextChoices):
        BOOKED = 'B', _('Booked'),
        NOT_BOOKED = 'N', _('Not_booked'),
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(choices=StatusChoices.choices, max_length=25, default=StatusChoices.BOOKED, )
    movie = models.ForeignKey(Movie, related_name="shows", on_delete=models.CASCADE)
    cinema_hall = models.ForeignKey(CinemaHall, related_name='shows', on_delete=models.CASCADE)

    def __str__(self):
        return "Show for " + str(self.movie) + " at " + str(self.cinema_hall)


class Booking(models.Model):
    class StatusChoices(models.TextChoices):
        BOOKED = 'B', _('Booked'),
        NOT_BOOKED = 'N', _('Not_booked'),
    number_of_seats = models.IntegerField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=StatusChoices.choices, max_length=25, default=StatusChoices.BOOKED, )
    show = models.ForeignKey(Show, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey('account.Account', related_name='show_seats', on_delete=models.CASCADE)


class ShowSeat(models.Model):
    class StatusChoices(models.TextChoices):
        BOOKED = 'B', _('Booked'),
        NOT_BOOKED = 'N', _('Not_booked'),
    status = models.CharField(choices=StatusChoices.choices, max_length=25, default=StatusChoices.BOOKED, )
    cinema_seat = models.ForeignKey(CinemaSeat, related_name='show_seats',on_delete=models.CASCADE)
    show = models.ForeignKey(Show, related_name='show_seats', on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, related_name='show_seats', on_delete=models.CASCADE)


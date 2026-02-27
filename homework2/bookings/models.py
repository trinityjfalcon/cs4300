from django.db import models
from django.contrib.auth.models import User


MAX_CHAR_LENGTH = 100
MAX_CHAR_DESCRIPTION_LENGTH = 300

class Movie(models.Model):
    title = models.CharField(max_length=MAX_CHAR_LENGTH)
    description = models.TextField(max_length=MAX_CHAR_DESCRIPTION_LENGTH)
    release_date = models.DateField()
    duration = models.FloatField()

class Seat(models.Model):
    class BookingStatus(models.TextChoices):
        AVAILABLE = "Available", "Available"
        UNAVAILABLE = "Unavailable", "Unavailable"

    seat_num = models.IntegerField()
    booking_status = models.CharField(
        max_length=100,
        choices=BookingStatus.choices,
        default=BookingStatus.AVAILABLE
    )

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)

from django.db import models

MAX_CHAR_LENGTH = 100
MAX_CHAR_DESCRIPTION_LENGTH = 300

class Movie(models.Model):
    title = models.CharField(max_length=MAX_CHAR_LENGTH)
    description = models.CharField(max_length=MAX_CHAR_DESCRIPTION_LENGTH)
    release_date = models.DateField()
    duration = models.FloatField()

class Seat(models.Model):
    seat_num = models.IntegerField()
    booking_status = models.TextChoices("Available", "Unavailable")

class Booking(models.Model):
    movie = models.CharField(max_length=MAX_CHAR_LENGTH)
    seat = models.IntegerField()
    user = models.CharField(max_length=MAX_CHAR_LENGTH)
    booking_date = models.DateField()

from django.shortcuts import render
from .models import Movie, Seat, Booking
from rest_framework import viewsets
from .serializers import MovieSerializers, SeatSerializer, BookingSerializer

"""
 ModelViewSet automatically provides list(), retrieve(), create(), update(),
 partial_update(), and destroy()
"""

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.MovieViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

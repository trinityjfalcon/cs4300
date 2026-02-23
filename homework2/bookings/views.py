from django.shortcuts import render
from .models import Movie, Seat, Booking
from rest_framework import viewsets
from .serializers import MovieSerializers, SeatSerializer, BookingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.MovieViewSet):
    queryset = Movie.objects.all()
    serializer_class = BookingSerializer

from django.shortcuts import render
from .models import Movie, Seat, Booking
from rest_framework import viewsets
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

"""
 ModelViewSet automatically provides list(), retrieve(), create(), update(),
 partial_update(), and destroy()
"""
# ViewSets for APIs
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Views for templates
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "bookings/movie_list.html", {"movies": Movie})

def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all()
    return render(request, "bookings/movie_list.html", {"movies": Movie, "seats": seats})
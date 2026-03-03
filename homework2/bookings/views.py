from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Seat, Booking
from rest_framework import viewsets
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.contrib import messages

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
    return render(request, "bookings/movie_list.html", {"movies": movies})

def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie)

    if request.method == "POST":
        # if user is not logged and and clicks book now, give error message
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to book a seat.")
            return redirect('login')

        seat_id = request.POST.get("seat_id")
        seat = get_object_or_404(Seat, id=seat_id)

        if seat.booking_status == Seat.BookingStatus.AVAILABLE:
            #Mark seat as unavailable
            seat.booking_status = Seat.BookingStatus.UNAVAILABLE
            seat.save()

            #Create the booking
            Booking.objects.create(
                movie=movie,
                seat=seat,
                user=request.user,
                booking_date=None
            )

        return redirect("book_seat", movie_id=movie_id)

    return render(request, "bookings/seat_booking.html", {"movie": movie, "seats": seats})

def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "bookings/booking_history.html", {"bookings": bookings})
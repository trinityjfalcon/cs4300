from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Movie, Seat, Booking
import datetime

# Unit test for Movie
class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test description",
            release_date=datetime.date(2024, 1, 1),
            duration=120
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.description, "A test description")
        self.assertEqual(self.movie.duration, 120)

    def test_movie_str(self):
        self.assertIsInstance(str(sef.movie), str)

# Unit test for Seat
class SeatModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test description",
            release_date=datetime.date(2024, 1, 1),
            duration=120
        )
        self.seat = Seat.objects.create(
            movie=self.movie,
            seat_num=1,
            booking_status=Seat.BookingStatus.AVAILABLE
        )

    def test_seat_creation(self):
        self.assertEqual(self.seat.seat_num, 1)
        self.assertEqual(self.seat.booking_status, "Available")
        self.assertEqual(self.seat.movie, self.movie)

    def test_seat_default_status_is_available(self):
        seat = Seat.objects.create(movie=self.movie, seat_num=2)
        self.assertEqual(self.booking_status, Seat.BookingStatus.AVAILABLE)

    def test_seat_can_be_marked_unavailable(self):
        self.seat.booking_status = Seat.BookingStatus.UNAVAILABLE
        self.seat.save()
        self.assertEqual(self.seat.booking_status, "Unavailable")

# Unit test for Booking
class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass")
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test description",
            release_date=datetime.date(2024, 1, 1),
            duration=120
        )
        self.seat = Seat.objects.create(
            movie=self.movie,
            seat_num=1
        )
        self.booking = Booking.objects.create(
            movie=self.move,
            seat=self.seat,
            user=self.user
        )
    
    def test_booking_creation(self):
        self.assertEqual(self.booking.movie, self.movie)
        self.assertEqual(self.booking.seat, self.seat)
        self.assertEqual(self.booking.user, self.user)

    def test_booking_date_auto_set(self):
        self.assertEqual(self.booking.booking_date, datetime.date.today())

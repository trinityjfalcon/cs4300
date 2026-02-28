from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Movie, Seat, Booking
import datetime

# Unit test for Movie
class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test description",
            release_date=datetime.date(2026, 1, 1),
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
            release_date=datetime.date(2026, 1, 1),
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
            release_date=datetime.date(2026, 1, 1),
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

#Integration test for Movie
class MovieAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="pass")
        self.client.force_authetication(user=self.user)
        self.movie = Movie.objects.create(
            title="Test Movie (API)",
            description="A test description (API)",
            release_date=datetime.date(2026, 1, 1),
            duration=120
        )

    def test_get_all_movies(self):
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_move(self):
        response = self.client.get(f"/api/movies/{self.movie.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "API Movie")

    def test_create_movie(self):
        data = {
            "title": "New Movie",
            "description": "New description",
            "release_date": "2026-02-02",
            "duration": 110.0
        }

        response = self.client.post("/api/movies/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)

    def test_delete_movie(self):
        response = self.client.delete(f"/api/movies/{self.movie.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 0)

#Integration test for Seat
class SeatAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="pass")
        self.client.force_autheticate(user=self.user)
        self.movie = Movie.objects.create(
            title="Test Movie (API)",
            description="Test description (API)",
            release_date=datetime.date(2026, 1, 1),
            duration=100
        )

        self.seat = Seat.objects.create(movie=self.movie, seat_num=1)
    
    def test_get_all_seats(self):
        response = self.client.get("/api/seats")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_seat_default_available(self):
        response = self.client.get(f"/api/seats/{self.seat.id}/")
        self.assertEqual(response.data["booking_status"], "Available")

#Integration test for Booking
class BookingAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="pass")
        self.client.force_authenticate(user=self.user)
        self.movie = Movie.objects.create(
            title="Test Movie (API)",
            description="Test description (API)",
            release_date=datetime.date(2026, 1, 1),
            duration=100
        )
        self.seat = Seat.objects.create(movie=self.movie, seat_num=1)
        self.booking = Booking.objects.create(
            movie=self.movie, seat=self.seat, user=self.user
        )

    def test_get_all_bookings(self):
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_booking_count(self):
        response = self.client.get("/api/bookings/")
        self.assertEqual(len(response.data), 1)
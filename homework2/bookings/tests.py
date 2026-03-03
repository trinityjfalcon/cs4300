from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Movie, Seat, Booking
import datetime

# Unit test for Movie
# Create a sample movie instance for tesing
class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test description",
            release_date=datetime.date(2026, 1, 1),
            duration=120
        )

    def test_movie_creation(self):
        # Verify movie fields are stored correctly
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.description, "A test description")
        self.assertEqual(self.movie.duration, 120)

    def test_movie_str(self):
        # ensure is string is returned
        self.assertIsInstance(str(self.movie), str)

# Unit test for Seat
class SeatModelTest(TestCase):
    def setUp(self):
        # create movie and seat
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
        # verify seat fields are correctly assigned
        self.assertEqual(self.seat.seat_num, 1)
        self.assertEqual(self.seat.booking_status, "Available")
        self.assertEqual(self.seat.movie, self.movie)

    def test_seat_default_status_is_available(self):
        # ensure default booking status is available
        seat = Seat.objects.create(movie=self.movie, seat_num=2)
        self.assertEqual(seat.booking_status, Seat.BookingStatus.AVAILABLE)

    def test_seat_can_be_marked_unavailable(self):
        # test updating booking status
        self.seat.booking_status = Seat.BookingStatus.UNAVAILABLE
        self.seat.save()
        self.assertEqual(self.seat.booking_status, "Unavailable")

# Unit test for Booking
class BookingModelTest(TestCase):
    def setUp(self):
        # create user, movie, seat, and booking instance
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
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )
    
    def test_booking_creation(self):
        # verify booking links correct movie, seat, and user
        self.assertEqual(self.booking.movie, self.movie)
        self.assertEqual(self.booking.seat, self.seat)
        self.assertEqual(self.booking.user, self.user)

    def test_booking_date_auto_set(self):
        # ensure booking date defaults to today's date
        self.assertEqual(self.booking.booking_date, datetime.date.today())

#Integration test for Movie
class MovieAPITest(TestCase):
    def setUp(self):
        # authenticate API client
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="pass")
        self.client.force_authenticate(user=self.user)
        
        # create initial movie
        self.movie = Movie.objects.create(
            title="Test Movie (API)",
            description="A test description (API)",
            release_date=datetime.date(2026, 1, 1),
            duration=120
        )

    def test_get_all_movies(self):
        # test retrieving list of movies
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_movie(self):
        #test retrieving specific movie by ID
        response = self.client.get(f"/api/movies/{self.movie.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Movie (API)")

    def test_create_movie(self):
        # test creating new movie via API
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
        # test deleting movie via api
        response = self.client.delete(f"/api/movies/{self.movie.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 0)

#Integration test for Seat
class SeatAPITest(TestCase):
    def setUp(self):
        # authenticate user and create test seat
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
    
    def test_get_all_seats(self):
        # test retrieve seats
        response = self.client.get("/api/seats", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_seat_default_available(self):
        # verify seat status is available through API
        response = self.client.get(f"/api/seats/{self.seat.id}/")
        self.assertEqual(response.data["booking_status"], "Available")

#Integration test for Booking
class BookingAPITest(TestCase):
    def setUp(self):
        # create booking for API testing
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
        # test retrieving bookings list
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_booking_count(self):
        # ensure 1 booking exists
        response = self.client.get("/api/bookings/")
        self.assertEqual(len(response.data), 1)

# View Tests
class ViewTests(TestCase):
    def setUp(self):
        # setup test client and sample data
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="pass")
        self.movie = Movie.objects.create(
            title="Test Movie (API)",
            description="Test description (API)",
            release_date=datetime.date(2026, 1, 1),
            duration=90
        )
        self.seat = Seat.objects.create(movie=self.movie, seat_num=1)

    def test_movie_list_view(self):
        # verify homepage loads successfully
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_book_seat_view_get(self):
        # verify booking page loads when logged in
        self.client.login(username="testuser", password="pass")
        response = self.client.get(f"/book/{self.movie.id}/")
        self.assertEqual(response.status_code, 200)

    def test_book_seat_post_books_seat(self):
        # verify seat booking updates status and booking record
        self.client.login(username="testuser", password="pass")
        response = self.client.post(f"/book/{self.movie.id}/", {"seat_id": self.seat.id})
        self.seat.refresh_from_db()
        self.assertEqual(self.seat.booking_status, "Unavailable")
        self.assertEqual(Booking.objects.count(), 1)

    def test_booking_history_view(self):
        #verify booking history page loads for logged-in user
        self.client.login(username="testuser", password="pass")
        response = self.client.get("/history/")
        self.assertEqual(response.status_code, 200)
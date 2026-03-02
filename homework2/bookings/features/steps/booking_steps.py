from behave import given, when, then
from django.contrib.auth.models import User
from django.test import Client
from bookings.models import Movie, Seat, Booking
import datetime

@given('I am on the homepage')
def step_homepage(context):
    context.client = Client()
    context.response = context.client.get('/')

@then('I should see the list of movies page')
def step_see_movie_list(context):
    assert context.response.status_code == 200

@given('I am a logged in user')
def step_logged_in(context):
    context.client = Client()
    context.user = User.objects.create_user(username='behaveuser', password='pass')
    context.client.login(username='behaveuser', password='pass')

@given('there is a movie with an available seat')
def step_available_seat(context):
    context.movie = Movie.objects.create(
        title='BDD Movie',
        description='BDD test',
        release_date=datetime.date(2026, 1, 1),
        duration=100
    )
    context.seat = Seat.objects.create(
        movie=context.movie,
        seat_num=1,
        booking_status=Seat.BookingStatus.AVAILABLE
    )

@when('I book the seat')
def step_book_seat(context):
    context.response = context.client.post(
        f'/book/{context.movie.id}/',
        {'seat_id': context.seat.id}
    )

@then('the seat should be marked as unavailable')
def step_seat_unavailable(context):
    context.seat.refresh_from_db()
    assert context.seat.booking_status == 'Unavailable'

@then('a booking should be created')
def step_booking_created(context):
    assert Booking.objects.filter(user=context.user).count() == 1

@given('I have an existing booking')
def step_booking_exists(context):
    context.movie = Movie.objects.create(
        title='Booking BDD Movie',
        description='Booking BDD test',
        release_date=datetime.date(2000, 1, 1),
        duration=101
    )
    context.seat = Seat.objects.create(
        movie=context.movie,
        seat_num=1
    )
    Booking.objects.create(
        movie=context.movie,
        seat=context.seat,
        user=context.user
    )

@when('I visit the booking history page')
def step_visit_history(context):
    context.response = context.client.get('/history/')

@then('I should see my booking')
def step_see_booking(context):
    assert context.response.status_code == 200
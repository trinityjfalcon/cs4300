from django.urls import path
from . import views

urlpatterns = [
    # Movie list page
    path('', views.movie_list, name='movie_list'),

    # Seat booking page
    path('book/<int:movie_id>/', views.book_seat, name='book_seat'),

    # Booking history page
    path('history/', views.booking_history, name='booking_history'),
]
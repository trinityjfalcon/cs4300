from django.urls import path
from . import views

urlpatterns = [
    # Movie list page
    path('', views.movie_list, name='movie_list'),

    # Booking history page
    path('book/<int:movie_id>/', views.book_seat, name='book_seat'),

    # Seat booking page
]
from rest_framework import serializers
from .models import Movie, Seat, Booking

"""
Serializers allow complex data like querysets and model instances 
to be converted to native Python datatypes and can be easily rendered
into JSON or other content types. Also handles deserialization.
"""

class MovieSerializer(serializers.ModelSerializer):
    """
    Uses ModelSerializer to automatically generate fields based on the
    Movie model definition
    """
    class Meta:
        model = Movie
        fields = '__all__'     #include all model fields in API

class SeatSerializer(serializers.ModelSerializer):
    """
    Converts Seat model instances to/from JSON format for API communication
    """
    class Meta:
        model = Seat
        fields = '__all__'   # Expose all seat fields

class BookingSerializer(serializers.ModelSerializer):
    """
    Handles validation and transformation of Booking data between JSON and
    Django model instances
    """
    class Meta:
        model = Booking
        fields = '__all__'

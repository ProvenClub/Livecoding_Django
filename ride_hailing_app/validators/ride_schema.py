
from rest_framework import serializers

class OfferRideSchema(serializers.Serializer):
    origin = serializers.CharField(max_length=255, required=True)
    destination = serializers.CharField(max_length=255, required=True)
    departure_time = serializers.DateTimeField(required=True)
    available_seats = serializers.IntegerField(min_value=1, required=True)
    price = serializers.FloatField(min_value=0, required=True)

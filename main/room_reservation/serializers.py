from rest_framework.serializers import ModelSerializer, CharField, PrimaryKeyRelatedField, ValidationError
from datetime import timedelta
import json

from room_reservation.services import check_rooms_is_booked

from .models import *

class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class GuestSerializer(ModelSerializer):
    full_name = CharField(read_only=True)
    class Meta:
        model = Guest
        fields = '__all__'


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'hotel', 'room_no']         


class BookingSerializer(ModelSerializer):
    rooms = PrimaryKeyRelatedField(queryset=Room.objects.all(), many=True)
    guest = GuestSerializer

    class Meta:
        model = Booking
        fields = ['id', 'guest', 'rooms', 'booking_date', 'arrival_date', 'duration']

    def validate(self, data):
            rooms = data['rooms']
            arrival_date = data['arrival_date']
            duration = data['duration']

            # CHECK WHETHER ROOMS LIST ARE BOOKED BEFORE
            result = check_rooms_is_booked(rooms, arrival_date, duration)
            if result != '':
                raise ValidationError(result)
            return data       
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response

from room_reservation.services import check_room_is_booked
from .models import *
from .serializers import *

class HotelViewset(ModelViewSet):
    queryset = Hotel.objects.all()

    permission_classes = [
        AllowAny
    ]

    serializer_class = HotelSerializer


class RoomViewset(ModelViewSet):
    queryset = Room.objects.all()

    permission_classes = [
        AllowAny
    ]

    serializer_class = RoomSerializer


class GuestViewset(ModelViewSet):
    queryset = Guest.objects.all()

    permission_classes = [
        AllowAny
    ]

    serializer_class = GuestSerializer


class BookingAPI(APIView):
    permission_classes = [AllowAny]

    # CREATE BOOKING
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:      
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    # READ BOOKING
    def get(self, request, uuid=None):
        if uuid:
            try:
                booking = Booking.objects.get(pk=uuid)
                serializer = BookingSerializer(booking)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


    # UPDATE BOOKING
    def put(self, request, uuid=None):
        try:
            booking = Booking.objects.get(pk=uuid)
            serializer = BookingSerializer(booking, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error2", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    # DELETE BOOKING
    def delete(self, request, uuid=None):
        try:
            booking = get_object_or_404(Booking, uuid=uuid)
            booking.delete()
            return Response({"status": "success", "data": "Booking Deleted"})
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    # CHECK WHETHER ROOM IS BOOKED BEFORE
    @api_view(['Get'])
    def check_room_booked(request, roomid, date):
        result = check_room_is_booked(roomid, date)
        if result == 0:
            return Response({"status": "success", "data": "Reserved"})
        elif result == 1:
            return Response({"status": "success", "data": "Not Reserved"})
        else:
            return Response({"status": "error", "data": "%s" % (result)}, status=status.HTTP_400_BAD_REQUEST)
        
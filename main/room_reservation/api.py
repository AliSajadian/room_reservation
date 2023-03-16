from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *
from room_reservation.services import check_room_is_booked

###### HotelAPI = CR , HotelDetailAPI = RUD ######
class HotelAPI(APIView):
    permission_classes = [
        AllowAny
    ]

    # CREATE HOTEL
    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:      
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    # READ HOTELS
    def get(self, request):
        guests = Hotel.objects.all()
        serializer = HotelSerializer(guests, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
class HotelDetailAPI(APIView):
    permission_classes = [
        AllowAny
    ]

    # READ HOTEL
    def get(self, request, pk=None):
        try:
            guest = Hotel.objects.get(pk=pk)
            serializer = HotelSerializer(guest)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                

    # UPDATE HOTEL
    def put(self, request, pk=None):
        try:
            guest = Hotel.objects.get(pk=pk)
            serializer = HotelSerializer(guest, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error2", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    # DELETE HOTEL
    def delete(self, request, pk=None):
        try:
            guest = get_object_or_404(Hotel, pk=pk)
            guest.delete()
            return Response({"status": "success", "data": "Hotel Deleted"})
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)


###### RoomAPI = CR , RoomDetailAPI = RUD ######
class RoomAPI(APIView):
    permission_classes = [
        AllowAny
    ]

    # CREATE ROOM
    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:      
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    # READ ROOMS
    def get(self, request):
        guests = Room.objects.all()
        serializer = RoomSerializer(guests, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
class RoomDetailAPI(APIView):
    permission_classes = [
        AllowAny
    ]

    # READ ROOM
    def get(self, request, pk=None):
        try:
            guest = Room.objects.get(pk=pk)
            serializer = RoomSerializer(guest)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                

    # UPDATE ROOM
    def put(self, request, pk=None):
        try:
            guest = Room.objects.get(pk=pk)
            serializer = RoomSerializer(guest, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error2", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    # DELETE ROOM
    def delete(self, request, pk=None):
        try:
            guest = get_object_or_404(Room, pk=pk)
            guest.delete()
            return Response({"status": "success", "data": "Room Deleted"})
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)


###### GuestAPI = CR , GuestDetailAPI = RUD ######
class GuestAPI(APIView):
    permission_classes = [
        AllowAny
    ]

    # CREATE GUEST
    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:      
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    # READ GUESTS
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
class GuestDetailAPI(APIView):
    permission_classes = [
        AllowAny

    ]

    # READ GUEST
    def get(self, request, pk=None):
        try:
            guest = Guest.objects.get(pk=pk)
            serializer = GuestSerializer(guest)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                

    # UPDATE GUEST
    def put(self, request, pk=None):
        try:
            guest = Guest.objects.get(pk=pk)
            serializer = GuestSerializer(guest, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error2", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    # DELETE GUEST
    def delete(self, request, pk=None):
        try:
            guest = get_object_or_404(Guest, pk=pk)
            guest.delete()
            return Response({"status": "success", "data": "Guest Deleted"})
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)


###### BookingAPI = CR , BookingDetailAPI = RUD ######
class BookingAPI(APIView):
    # basename = 'booking'
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
    def get(self, request):        
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
class BookingDetailAPI(APIView):
    # basename = 'booking'
    permission_classes = [AllowAny]

    # READ BOOKING
    def get(self, request, pk=None):
        try:
            booking = Booking.objects.get(pk=pk)
            serializer = BookingSerializer(booking)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                

    # UPDATE BOOKING
    def put(self, request, pk=None):
        try:
            booking = Booking.objects.get(pk=pk)
            serializer = BookingSerializer(booking, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error2", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    # DELETE BOOKING
    def delete(self, request, pk=None):
        try:
            booking = get_object_or_404(Booking, pk=pk)
            booking.delete()
            return Response({"status": "success", "data": "Booking Deleted"})
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    # CHECK WHETHER ROOM IS BOOKED BEFORE
    @api_view(['Get'])
    def check_room_booked(request, roomid, date):
        result = check_room_is_booked(roomid, date)
        return Response({"status": "checked", "data": result}, status=status.HTTP_200_OK)

        
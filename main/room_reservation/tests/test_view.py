
import json
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from ..models import *
from ..serializers import *
from ..api import *

class APIUrlsTest(APITestCase):
    def test_get_guests_is_resolved(self):
        url = reverse('guest')
        self.assertEquals(resolve(url).func.view_class, GuestAPI)

# # Testing read all http Get method, and create by Post http method 
# class HotelAPITest(APITestCase):
#     # Create user and credentials
#     def setUp(self):
#         self.url = reverse('hotel')
#         self.user = User.objects.create_user(username='admin', password='admin1234')
#         self.token = Token.objects.create(user=self.user)    
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

#     #  Check Get hotels authentication
#     def test_get_hotels_authenticated(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     #  Check Get hotels un authentication
#     def test_get_hotels_un_authenticated(self):
#         self.client.force_authenticate(user=None, token=None)
#         response = self.client.get(self.url)
#         self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

#     # Check create hotel authentication
#     def test_post_hotel_authenticated(self):
#         data = {
#             "name": "Royal"
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(len(response.data), 8)
# # Testing read http Get method, and update by Put http method and delete by Delete http method
# class HotelDetailAPITest(APITestCase):
#     hotel_url = reverse('hotel-detail', args=[1])
#     hotels_url = reverse('hotel')
#     # Create user and credentials
#     def setUp(self):
#         self.user = User.objects.create_user(username='admin', password='admin1234')
#         self.token = Token.objects.create(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

#         data= {
#             "name": "Royal" 
#         }
#         self.client.post(self.hotels_url, data, format='json')

#     #  Check Get hotel authentication
#     def test_get_hotel_authenticated(self):
#         response = self.client.get(self.hotel_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['name'], 'Royal')

#     #  Check Get hotel un authentication
#     def test_get_hotel_un_authenticated(self):
#         self.client.force_authenticate(user=None, token=None)
#         response = self.client.get(self.hotel_url)
#         self.assertEqual(response.status_code, 403)

#     #  Check update hotel un authentication
#     def test_delete_hotel_authenticated(self):
#         response = self.client.update(self.hotel_url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     #  Check delete hotel un authentication
#     def test_delete_hotel_authenticated(self):
#         response = self.client.delete(self.hotel_url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class HotelTest(APITestCase):
    hotel_url = reverse('hotel')
    def setUp(self):
        self.royal = Hotel.objects.create(name='Royal')
        self.star_light = Hotel.objects.create(name='Star Light')
        self.magical_travel = Hotel.objects.create(name='Magical Travel')
        self.create_valid_payload = {
            'name': 'China'
        }
        self.update_valid_payload = {
            'name': 'Royal'
        }
        self.invalid_payload = {
            'name': ''
        }

    def test_get_all_hotels(self):
        response = self.client.get(self.hotel_url)
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_hotel(self):
        response = self.client.get(reverse('hotel-detail', kwargs={'pk': self.royal.pk}))
        hotel = Hotel.objects.get(pk=self.royal.pk)
        serializer = HotelSerializer(hotel)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_hotel(self):
        response = self.client.get(reverse('hotel-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_hotel(self):
        response = self.client.post(
            self.hotel_url,
            data=json.dumps(self.create_valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_hotel(self):
        response = self.client.post(
            self.hotel_url,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_hotel(self):
        Response = self.client.put(
            reverse('hotel-detail', args=[self.royal.pk]),
            data=json.dumps(self.update_valid_payload),
            content_type='application/json'
        )
        self.assertEqual(Response.status_code, status.HTTP_200_OK)

    def test_invalid_update_hotel(self):
        Response = self.client.put(
            reverse('hotel-detail', args=[self.royal.pk]),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(Response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_hotel(self):
        response = self.client.delete(
            reverse('hotel-detail', kwargs={'pk': self.star_light.pk})
        ) 
        # print('------------------------------------')
        # print(Hotel.objects.all())
        # print(response)
        # print('------------------------------------')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete_hotel(self):
        response = self.client.delete(
            reverse('hotel-detail', args=[350])
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class GuestTest(APITestCase):
    guest_url = reverse('guest')
    def setUp(self):
        self.john = Guest.objects.create(first_name='john', last_name='sean')
        self.jean = Guest.objects.create(first_name='jean', last_name='parker')
        self.tom = Guest.objects.create(first_name='tom', last_name='hangs')
        self.create_valid_payload = {
            'first_name': 'suzan',
            'last_name': 'smith'
        }
        self.update_valid_payload = {
            'first_name': 'john',
            'last_name': 'sean'
        }
        self.invalid_payload = {
            'first_name': '',
            'last_name': ''
        }

    def test_get_all_guests(self):
        response = self.client.get(self.guest_url)
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_guest(self):
        response = self.client.get(reverse('guest-detail', kwargs={'pk': self.john.pk}))
        guest = Guest.objects.get(pk=self.john.pk)
        serializer = GuestSerializer(guest)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_guest(self):
        response = self.client.get(reverse('guest-detail', kwargs={'pk': 350}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_guest(self):
        response = self.client.post(
            self.guest_url,
            data=json.dumps(self.create_valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_guest(self):
        response = self.client.post(
            self.guest_url,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_guest(self):
        Response = self.client.put(
            reverse('guest-detail', args=[self.john.pk]),
            data=json.dumps(self.update_valid_payload),
            content_type='application/json'
        )
        self.assertEqual(Response.status_code, status.HTTP_200_OK)

    def test_invalid_update_guest(self):
        Response = self.client.put(
            reverse('guest-detail', args=[self.john.pk]),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(Response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_guest(self):
        response = self.client.delete(
            reverse('guest-detail', kwargs={'pk': self.tom.pk})
        ) 
        # print('------------------------------------')
        # print(Hotel.objects.all())
        # print(response)
        # print('------------------------------------')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete_guest(self):
        response = self.client.delete(
            reverse('guest-detail', args=[30])
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class RoomTest(APITestCase):
    room_url = reverse('room')
    def setUp(self):
        self.china_hotel = Hotel.objects.create(name='chian hotel')
        self.room1 = Room.objects.create(hotel=self.china_hotel, room_no=1)
        self.room2 = Room.objects.create(hotel=self.china_hotel, room_no=2)
        self.room3 = Room.objects.create(hotel=self.china_hotel, room_no=3)
        self.create_valid_payload = {
            'hotel': self.china_hotel.pk,
            'room_no': 4
        }
        self.update_valid_payload = {
            'hotel': self.china_hotel.pk,
            'room_no': 7
        }
        self.invalid_payload = {
            'hotel': '',
            'room_no': 5
        }

    def test_get_all_rooms(self):
        response = self.client.get(self.room_url)
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_room(self):
        response = self.client.get(reverse('room-detail', kwargs={'pk': self.room1.pk}))
        room = Room.objects.get(pk=self.room1.pk)
        serializer = RoomSerializer(room)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_room(self):
        response = self.client.get(reverse('room-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_room(self):
        response = self.client.post(
            self.room_url,
            data=json.dumps(self.create_valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_room(self):
        response = self.client.post(
            self.room_url,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_room(self):
        response = self.client.put(
            reverse('room-detail', args=[self.room1.pk]),
            data=json.dumps(self.update_valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_room(self):
        Response = self.client.put(
            reverse('room-detail', args=[self.room1.pk]),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(Response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_room(self):
        response = self.client.delete(
            reverse('room-detail', kwargs={'pk': self.room2.pk})
        ) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete_room(self):
        response = self.client.delete(
            reverse('room-detail', args=[30])
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class BookingTest(APITestCase):
    booking_url = reverse('booking')
    def setUp(self):
        self.china_hotel = Hotel.objects.create(name='chian hotel')
        self.room1 = Room.objects.create(hotel=self.china_hotel, room_no=1)
        self.room2 = Room.objects.create(hotel=self.china_hotel, room_no=2)
        self.room3 = Room.objects.create(hotel=self.china_hotel, room_no=3)
        self.john = Guest.objects.create(first_name='john', last_name='sean')
        self.jean = Guest.objects.create(first_name='jean', last_name='parker')

        self.booking1 = Booking.objects.create(guest=self.john, booking_date='2023-03-16', arrival_date='2023-03-18', duration=2)
        self.booking1.rooms.set(Room.objects.filter(pk = self.room1.pk))
        self.booking2 = Booking.objects.create(guest=self.jean, booking_date='2023-03-16', arrival_date='2023-03-20', duration=1)
        self.booking2.rooms.set(Room.objects.filter(pk = self.room3.pk))

        self.create_valid_payload = {
            'guest': self.jean.pk,
            'rooms': [self.room2.pk],
            'booking_date': '2023-03-16',
            'arrival_date': '2023-03-25',
            'duration': 2
        }
        self.update_valid_payload = {
            'guest': self.john.pk,
            'rooms': [self.room3.pk],
            'booking_date': '2023-03-16',
            'arrival_date': '2023-03-18',
            'duration': 1
        }
        self.invalid_payload = {
            'guest': '',
            'rooms': [],
            'booking_date': '2023-03-16',
            'arrival_date': '',
            'duration': ''
        }

    def test_get_all_bookings(self):
        response = self.client.get(self.booking_url)
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_booking(self):
        response = self.client.get(reverse('booking-detail', kwargs={'pk': self.booking1.pk}))
        booking = Booking.objects.get(pk=self.booking1.pk)
        serializer = BookingSerializer(booking)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_booking(self):
        response = self.client.get(reverse('booking-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_booking(self):
        response = self.client.post(
            self.booking_url,
            data=json.dumps(self.create_valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_booking(self):
        response = self.client.post(
            self.booking_url,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_booking(self):
        response = self.client.put(
            reverse('booking-detail', args=[self.booking1.pk]),
            data=json.dumps(self.update_valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_booking(self):
        response = self.client.put(
            reverse('booking-detail', args=[self.booking1.pk]),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_booking(self):
        response = self.client.delete(
            reverse('booking-detail', kwargs={'pk': self.booking2.pk})
        ) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete_booking(self):
        response = self.client.delete(
            reverse('booking-detail', args=[30])
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

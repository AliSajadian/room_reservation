from rest_framework.test import APITestCase
from ..models import Hotel, Room


class HotelRoomTest(APITestCase):
    """ Test module for Hotel & Room model """

    def setUp(self):
        Hotel.objects.create(name='Royal')
        Hotel.objects.create(name='Star Light')
        hotel_royal=Hotel.objects.get(name='Royal')

        Room.objects.create(
            hotel=hotel_royal, room_no=1)
        Room.objects.create(
            hotel=hotel_royal, room_no=2)

    def test_room_hotel_name(self):
        hotel_royal = Hotel.objects.get(name='Royal')
        hotel_starlight = Hotel.objects.get(name='Star Light')

        self.assertEqual(
            hotel_royal.__str__(), "Royal")
        self.assertEqual(
            hotel_starlight.__str__(), "Star Light")

        room_royal_1 = Room.objects.get(room_no=1)
        room_royal_2 = Room.objects.get(room_no=2)
           
        self.assertEqual(
            room_royal_1.hotel_name(), "Royal")
        self.assertEqual(
            room_royal_2.hotel_name(), "Royal")

        self.assertEqual(
            room_royal_1.__str__(), "1")
        self.assertEqual(
            room_royal_2.__str__(), "2")
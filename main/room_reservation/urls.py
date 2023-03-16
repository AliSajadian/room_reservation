from rest_framework import routers
from django.urls import path, include
from rest_framework.response import Response

from .api import *

class DocsView(APIView):
    """
    Documentation of Room Reservation RESTFul API
    """
    def get(self, request, *args, **kwargs):
        end_points = {'api/hotel': request.build_absolute_uri('api/hotel/'),
                      'api/hotel/<pk>/': request.build_absolute_uri('api/hotel/1/'),
                      'api/room': request.build_absolute_uri('api/room/'),
                      'api/room/<pk>/': request.build_absolute_uri('api/room/1/'),
                      'api/guest': request.build_absolute_uri('api/guest/'),
                      'api/guest/<pk>/': request.build_absolute_uri('api/guest/1/'),
                      'api/booking': request.build_absolute_uri('api/booking/'),
                      'api/booking/<pk>/': request.build_absolute_uri('api/booking/1/'),
                      'api/checkroombooked/<roomid>/<date>/': request.build_absolute_uri('api/checkroombooked/1/2023-03-10/'),
                     }
        return Response(end_points)

router = routers.DefaultRouter()
 
urlpatterns=[
    path('', DocsView.as_view()),
    path('', include(router.urls)),
    path('api/hotel/', HotelAPI.as_view(), name='hotel'),
    path('api/hotel/<int:pk>/', HotelDetailAPI.as_view(), name='hotel-detail'),
    path('api/room/', RoomAPI.as_view(), name='room'),
    path('api/room/<int:pk>/', RoomDetailAPI.as_view(), name='room-detail'),
    path('api/guest/', GuestAPI.as_view(), name='guest'),
    path('api/guest/<int:pk>/', GuestDetailAPI.as_view(), name='guest-detail'),
    path('api/booking/', BookingAPI.as_view(), name='booking'),
    path('api/booking/<int:pk>/', BookingDetailAPI.as_view(), name='booking-detail'),
    path('api/checkroombooked/<int:roomid>/<str:date>/', BookingDetailAPI.check_room_booked, name='checkroombooked/<roomid>/<date>/'),
]

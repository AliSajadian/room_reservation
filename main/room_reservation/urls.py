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
                      'api/room': request.build_absolute_uri('api/room/'),
                      'api/guest': request.build_absolute_uri('api/guest/'),
                      'api/booking': request.build_absolute_uri('api/booking'),
                      'api/booking/<id>/': request.build_absolute_uri('api/booking/1/'),
                      'api/checkroombooked/<roomid>/<date>/': request.build_absolute_uri('api/checkroombooked/1/2023-03-10/'),
                     }
        return Response(end_points)


router = routers.DefaultRouter()
router.register('api/hotel', HotelViewset, 'hotel')
router.register('api/room', RoomViewset, 'room')
router.register('api/guest', GuestViewset, 'guest')
 
urlpatterns=[
    path('', DocsView.as_view()),
    path('', include(router.urls)),
    path('api/booking', BookingAPI.as_view()),
    path('api/booking/<str:uuid>/', BookingAPI.as_view()),
    path('api/checkroombooked/<int:roomid>/<str:date>/', BookingAPI.check_room_booked, name='checkroombooked/<roomid>/<date>/'),
]

urlpatterns += router.urls
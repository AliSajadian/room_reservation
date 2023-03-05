from datetime import datetime, timedelta 
import pandas as pd

from room_reservation.models import *

# CHECK WHETHER ROOM IS BOOKED BEFORE
def check_room_is_booked(_room_id, _date):
    try:
        room = Room.objects.filter(pk=_room_id)
        if not len(room):
            return 'room id %s does not exist.' % (_room_id)

        bookings = Booking.objects.filter(rooms__pk=_room_id)
        if not len(bookings):
            return 'room no. %s is not booked at all.' % (room[0].room_no)

        check_date = datetime.strptime(_date, '%Y-%m-%d').date()

        for booking in bookings: 
            duration = booking.duration
            arrival_date = booking.arrival_date
            departure_date = arrival_date + timedelta(duration - 1)

            if arrival_date <= check_date and check_date <= departure_date:
                return 'room no.%s was reserved before in date %s.' % (room[0].room_no, check_date)

        return 'room no.%s in date %s is not booked.' % (room[0].room_no, check_date)
    except Exception as e:
        return str(e)


# CHECK WHETHER ROOMS LIST ARE BOOKED BEFORE
def check_rooms_is_booked(_rooms, _arrival_date, _duration):
    try:
        for room_id in _rooms:
            id = str(room_id)

            room = Room.objects.filter(pk=id)
            if not len(room):
                continue

            bookings = Booking.objects.filter(rooms__pk=id)
            if not len(bookings):
                continue

            start_date = _arrival_date
            end_date = start_date + timedelta(_duration - 1)
            date_range = pd.date_range(start_date, end_date)

            for booking in bookings:
                arrival_date = booking.arrival_date
                duration = booking.duration
                departure_date = arrival_date + timedelta(duration - 1)

                for check_date in date_range:
                    check_date = check_date.date()

                    if arrival_date <= check_date and check_date <= departure_date:
                        return 'room no.%s was reserved before in date %s' % (room[0].room_no, check_date)

        return ''
    except Exception as e:
        return str(e)
        
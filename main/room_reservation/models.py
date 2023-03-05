from django.db import models
from datetime import datetime, timedelta


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    # ..rest fields
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ''
        db_table = 'tbl_rez_hotel'


class EmployeeType(models.Model):
    name = models.CharField(max_length=100)
    # ..rest fields
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_rez_employee_type'


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    # ..rest fields
    objects = models.Manager()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        db_table = 'tbl_rez_employee'


class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # ...rest fields
    objects = models.Manager()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        db_table = 'tbl_rez_Guest'

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Agent(models.Model):
    name = models.CharField(max_length=100)
    # ...rest fields
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_rez_guest'


class RoomType(models.Model):
    name = models.CharField(max_length=100)
    # ..rest fields
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_rez_room_type'


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='hotel_room', on_delete=models.PROTECT)
    room_no = models.IntegerField()
    # ...rest fields
    objects = models.Manager()

    def __str__(self):
        return str(self.room_no)

    def hotel_name(self):
        return self.hotel.name
        
    class Meta:
        db_table = 'tbl_rez_room'


class Booking(models.Model):
    guest = models.ForeignKey(Guest, related_name='booking_guest', on_delete=models.PROTECT)
    rooms = models.ManyToManyField(Room, related_name='booking_room')
    booking_date = models.DateTimeField(default=datetime.now)
    arrival_date = models.DateField()
    duration = models.SmallIntegerField()
    # ...rest fields
    objects = models.Manager()

    def __str__(self):
        return self.guest.full_name

    class Meta:
        db_table = 'tbl_rez_booking'
        

class Payment(models.Model):
    amount = models.IntegerField()
    # ...rest fields
    objects = models.Manager()

    class Meta:
        db_table = 'tbl_rez_payment'

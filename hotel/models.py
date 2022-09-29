from django.db import models
from django.conf import settings
from django.urls import reverse_lazy


class Room(models.Model):
    ROOM_CATEGORIES=(  
        ('CLASSIC', 'CLASSIC-NEST'),
        ('SUPER', 'SUPER-NEST'),
        ('EXECUTIVE', 'EXECUTIVE-NEST'),
        ('TWIN', 'TWIN-NEST'),
        ('ROYAL', 'ROYAL-NEST'),
        
    )
    number = models.IntegerField()
    category = models.CharField(max_length=10, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    detail = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.number}. {self.category}'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f' {self.user} " has booked -" {self.room} "- from - " {self.check_in} " - to - " {self.check_out}'

    def get_room_category(self):
        room_categories = dict(self.room.ROOM_CATEGORIES)
        room_category = room_categories.get(self.room.category)
        return room_category

    def get_cancel_booking_url(self):
        return reverse_lazy('hotel:CancelBookingView', args=[self.pk])
        
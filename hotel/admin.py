from django.contrib import admin
from .models import Room, Booking

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'check_in', 'check_out',)
    search_fields = ('user', 'room', 'check_in', 'check_out',)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'category', 'beds', 'capacity',)

admin.site.register(Room, RoomAdmin)

admin.site.register(Booking, HotelAdmin)
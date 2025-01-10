from django.contrib import admin
from .models import Reservation, ParkingSpot

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'datetime')


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'status')



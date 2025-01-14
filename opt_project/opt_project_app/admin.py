from django.contrib import admin
from .models import Reservation, ParkingSpot

# Register your models here.
@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'status', 'reserver')  # Display parking spot details
    list_filter = ('status',)  # Filter by parking spot status
    search_fields = ('number', 'status', 'reserver__username')  # Add search functionality


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'parking_spot', 'start_time', 'end_time')  # Display key details
    list_filter = ('parking_spot', 'user', 'start_time', 'end_time')  # Add filtering options
    search_fields = ('title', 'user__username', 'parking_spot__number')  # Add search functionality


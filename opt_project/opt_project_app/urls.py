from django.urls import path
from . import views

urlpatterns = [
    path('reservations/', views.get_reservations, name='get_reservations'),
    path('reservations/create/', views.create_reservation, name='create_reservation'),
    path('reservations/delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('spots/', views.get_parking_spots, name='get_parking_spots'),
]

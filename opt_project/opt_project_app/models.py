from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ParkingSpot(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    status = models.CharField(max_length=20) # Free | Reserved | Occupied
    reserver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who made the reservation
    title = models.CharField(max_length=200)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.title} : on number {self.parking_spot.number} - {self.start_time} to {self.end_time}"
    


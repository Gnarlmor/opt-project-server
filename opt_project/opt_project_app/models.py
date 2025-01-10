from django.db import models

# Create your models here.
class Reservation(models.Model):
    # Fields for the table
    id = models.AutoField(primary_key=True)  # Auto-incrementing unique ID
    title = models.CharField(max_length=200)  # Title of the reservation
    datetime = models.DateTimeField()  # Date and time of the reservation

    def __str__(self):
        return f"{self.title} on {self.datetime}"
    
class ParkingSpot(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    status = models.CharField(max_length=20) # Free | Reserved | Occupied

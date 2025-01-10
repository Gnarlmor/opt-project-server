from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reservation, ParkingSpot
import json

# Get all reservations
def get_reservations(request):
    if request.method == 'GET':
        reservations = list(Reservation.objects.values())  # Convert QuerySet to a list of dictionaries
        return JsonResponse(reservations, safe=False)  # Return as JSON

# Create a new reservation
@csrf_exempt
def create_reservation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON body
            title = data.get('title')
            datetime = data.get('datetime')
            reservation = Reservation.objects.create(title=title, datetime=datetime)
            return JsonResponse({'id': reservation.id, 'title': reservation.title, 'datetime': reservation.datetime})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# Delete a reservation
@csrf_exempt
def delete_reservation(request, reservation_id):
    if request.method == 'DELETE':
        try:
            reservation = Reservation.objects.get(id=reservation_id)
            reservation.delete()
            return JsonResponse({'message': 'Reservation deleted successfully'})
        except Reservation.DoesNotExist:
            return JsonResponse({'error': 'Reservation not found'}, status=404)

# Get all parking spots
def get_parking_spots(request):
    if request.method == 'GET':
        spots = list(ParkingSpot.objects.values())  # Convert QuerySet to a list of dictionaries
        return JsonResponse(spots, safe=False)  # Return as JSON
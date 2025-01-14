from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reservation, ParkingSpot
from django.contrib.auth.models import User
import json

# Get all reservations
def get_reservations(request):
    if request.method == 'GET':
        reservations = list(Reservation.objects.values(
            'id', 'title', 'user__username', 'parking_spot__number', 'start_time', 'end_time'
        ))  # Retrieve fields, including related user and parking spot details
        return JsonResponse(reservations, safe=False)  # Return as JSON

# Create a new reservation
@csrf_exempt
def create_reservation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON body
            user_id = data.get('user_id')  # Pass user ID in the request
            parking_spot_id = data.get('parking_spot_id')  # Pass parking spot ID in the request
            title = data.get('title')
            start_time = data.get('start_time')  # Pass start time as ISO 8601 string
            end_time = data.get('end_time')  # Pass end time as ISO 8601 string

            # Get User and ParkingSpot objects
            user = User.objects.get(id=user_id)
            parking_spot = ParkingSpot.objects.get(id=parking_spot_id)

            # Create reservation
            reservation = Reservation.objects.create(
                user=user,
                parking_spot=parking_spot,
                title=title,
                start_time=start_time,
                end_time=end_time
            )

            # Set parking spot status to Reserved and the reserver to the user
            parking_spot.status = 'Reserved'
            parking_spot.reserver = user

            # Return the created reservation as JSON
            return JsonResponse({
                'id': reservation.id,
                'title': reservation.title,
                'user': reservation.user.username,
                'parking_spot': reservation.parking_spot.number,
                'start_time': reservation.start_time,
                'end_time': reservation.end_time
            })

        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except ParkingSpot.DoesNotExist:
            return JsonResponse({'error': 'Parking spot not found'}, status=404)
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
        spots = list(ParkingSpot.objects.values(
            'id', 'number', 'status', 'reserver__username'
        ))  # Include reserver details
        return JsonResponse(spots, safe=False)  # Return as JSON

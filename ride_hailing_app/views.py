
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services.ride_service import RideService
from .validators.ride_schema import OfferRideSchema
import json

@csrf_exempt
def offer_ride(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            schema = OfferRideSchema(data=data)
            if schema.is_valid():
                result = RideService.offer_ride(schema.validated_data)
                return JsonResponse(result, status=200)
            else:
                return JsonResponse({'errors': schema.errors}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Failed to process request', 'message': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

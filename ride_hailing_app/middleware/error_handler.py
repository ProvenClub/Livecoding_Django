
from django.http import JsonResponse

class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except Exception as e:
            # General error handling logic
            return JsonResponse({'error': 'Internal Server Error', 'message': str(e)}, status=500)

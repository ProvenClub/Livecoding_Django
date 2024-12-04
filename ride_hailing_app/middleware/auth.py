
from django.http import JsonResponse

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.headers.get('user-id')
        if not user_id:
            return JsonResponse({'error': 'Authentication required'}, status=401)
        request.user_id = user_id
        return self.get_response(request)

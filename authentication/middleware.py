from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from .models import BlacklistedAccessToken

class TokenBlacklistMiddleware(MiddlewareMixin):
    def process_request(self, request):
        authorization_header = request.headers.get('Authorization', '')
        if authorization_header.startswith('Bearer '):
            token = authorization_header.split('Bearer ')[1]
            if BlacklistedAccessToken.objects.filter(token=token).exists():
                return JsonResponse({'detail': 'Token is blacklisted'}, status=401)
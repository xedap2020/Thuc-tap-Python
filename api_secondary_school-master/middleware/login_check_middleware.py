from django.http import JsonResponse
import jwt
from user.models import User
from base.api.exceptions import CreateFail
import requests

class LoginCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def decode_user(self, token):
        user = jwt.decode(jwt=token, key='secret', algorithms=["HS256"])
        return user

    def __call__(self, request):
        try:
            public_paths = [
                '/api/school-years/',
                '/api/subjects/',
                '/api/classes/',
                '/api/grades/',
                # 'api/users/',
                '/api/departments/',
                # 'api/students/',
                '/api/class-subjects/',
                # 'api//points/',
                '/api/personal/login',
            ]
            if request.path not in public_paths:
                token = request.headers['Authorization'] if 'Authorization' in request.headers else None
                if not token:
                    return JsonResponse({'error': 'Unauthorized'}, status=401)
                token = token.split(' ')[1]
                payload = self.decode_user(token)
                user = User.objects.get(pk=payload['id'])
                if not user or user.position == 'Giáo viên':
                    return JsonResponse({'error': 'Not permission'}, status=403)

            response = self.get_response(request)
            return response
        except Exception as e:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

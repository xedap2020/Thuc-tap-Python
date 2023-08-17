import bcrypt
import jwt
import re
import datetime
from rest_framework import generics
from rest_framework import views
from base.api.response import SuccessResponse, ValidationErrorResponse, Response
from base.api.exceptions import CreateFail, UpdateFail, DeleteFail, NotFound
from user.models import User
from .serializers import TokenSerializer
from django.http import JsonResponse

class Login(views.APIView):
    permission_class = []

    def hash_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')

    def concatenate_content(self, match):
        return match.group(1)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            credentials = {
                'phone': data.get('phone'),
                'password': data.get('password'),
            }

            if not credentials['phone'] or not credentials['password']:
                return JsonResponse({
                    "error": {
                        "code": 400,
                        "message": "Invalid parameters"
                    }
                }, status=400)

            user = User.objects.filter(phone=credentials['phone']).first()
            if not user:
                raise NotFound

            if not bcrypt.checkpw(credentials['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({
                    "error": {
                        "code": 400,
                        "message": "Password is incorrect"
                    }
                }, status=400)

            token = jwt.encode({
                "id": user.id,
                "full_name": user.full_name,
                "phone": user.phone,
                "email": user.email,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=12)
                }, 
                "secret",
                algorithm="HS256"
            )

            pattern = r"'(.*?)'"
            match = re.search(pattern, str(token))

            if match:
                token = match.group(1)

            serializer = TokenSerializer({'token': token})
            return SuccessResponse(data=serializer.data)
        except Exception:
            return JsonResponse({
                "error": {
                    "code": 500,
                    "message": "Internal Server Error"
                }
            }, status=500)

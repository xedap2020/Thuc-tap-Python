from rest_framework import generics
from rest_framework import views
from base.api.pagination import Pagination
from base.api.response import SuccessResponse, ValidationErrorResponse, Response
from base.api.exceptions import CreateFail, UpdateFail, DeleteFail, NotFound
from ..models import User
from .serializers import UserSerializer, ListUserSerializer, UserCreateSerializer
from department.models import Department
import bcrypt

class UserList(generics.ListAPIView):
    serializer_class = ListUserSerializer
    pagination_class = Pagination
    queryset = User.objects.order_by('-created_at')


class UserDetail(generics.RetrieveAPIView):
    serializer_class = ListUserSerializer
    queryset = User.objects.all()


class AddUser(views.APIView):
    permission_class = []

    def hash_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')

    def post(self, request, format=None):
        try:
            data = request.data
            user = {
                'full_name': data.get('full_name'),
                'address': data.get('address'),
                'email': data.get('email'),
                'phone': data.get('phone'),
                'email': data.get('email'),
                'position': data.get('position'),
                'specialize': data.get('specialize'),
                'department': data.get('department_id'),
                'password': self.hash_password(data.get('password')),
            }
            if not user['full_name'] or not user['phone'] or not user['password']:
                return Response({'detail': 'Invalid parameters'}, status=400)

            if user['department']:
                find_department = Department.objects.get(id=user['department'])
                if not find_department:
                    return Response({'detail': 'department_id is invalid'}, status=400)

            serializer = UserCreateSerializer(data=user)

            if not serializer.is_valid():
                return ValidationErrorResponse(data=serializer.data)

            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Exception:
            raise CreateFail


class EditUser(generics.UpdateAPIView):
    permission_class = []

    def get_object(self):
        try:
            return User.objects.get(id=self.kwargs["pk"])
        except User.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if not instance:
                raise NotFound
                
            data = request.data
            user = {
                'full_name': data.get('full_name'),
                'address': data.get('address'),
                'email': data.get('email'),
                'position': data.get('position'),
                'specialize': data.get('specialize'),
                'department': data.get('department_id'),
            }
            serializer = UserSerializer(instance, data=user)

            if not serializer.is_valid():
                return ValidationErrorResponse(data=serializer.errors)
                
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Exception:
            raise UpdateFail


class DeleteUser(generics.DestroyAPIView):
    permission_class = []

    def get_object(self):
        try:
            return User.objects.get(id=self.kwargs['pk'])
        except User.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
            if not obj:
                raise NotFound
            obj.delete()
            return SuccessResponse(message='Delete success')
        except Exception:
            raise DeleteFail

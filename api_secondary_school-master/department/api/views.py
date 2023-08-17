from rest_framework import generics
from rest_framework import views
from base.api.pagination import Pagination
from ..models import Department
from .serializers import DepartmentSerializer, ListDepartmentSerializer
from base.api.response import SuccessResponse, ValidationErrorResponse
from base.api.exceptions import CreateFail, UpdateFail, DeleteFail, NotFound


class CustomPagination(Pagination):
    default_limit = 20
    max_limit = 20


class DepartmentList(generics.ListAPIView):
    serializer_class = ListDepartmentSerializer
    pagination_class = CustomPagination
    queryset = Department.objects.all()


class DepartmentDetail(generics.RetrieveAPIView):
    serializer_class = ListDepartmentSerializer
    queryset = Department.objects.all()


class AddDepartment(views.APIView):
    permission_class = []

    def post(self, request, format=None):
        data = request.data
        department = {
            'name': data.get('name'),
        }
        serializer = DepartmentSerializer(data=department)
        if not serializer.is_valid():
            return ValidationErrorResponse(data=serializer.data)
        try:
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Exception:
            raise CreateFail


class EditDepartment(generics.UpdateAPIView):
    permission_class = []

    def get_object(self):
        try:
            return Department.objects.get(id=self.kwargs["pk"])
        except Department.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if not instance:
                raise NotFound
            data = request.data
            department = {
                'name': data.get('name'),
            }
            serializer = DepartmentSerializer(instance, data=department)
            if not serializer.is_valid():
                return ValidationErrorResponse(data=serializer.errors)
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Exception:
            raise UpdateFail


class DeleteDepartment(generics.DestroyAPIView):
    permission_class = []

    def get_object(self):
        try:
            return Department.objects.get(id=self.kwargs['pk'])
        except Department.DoesNotExist:
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









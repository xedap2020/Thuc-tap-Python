from rest_framework import generics
from rest_framework import views
from base.api.pagination import Pagination
from ..models import SchoolYear
from .serializers import SchoolYearSerializer, ListSchoolYearSerializer
from base.api.response import SuccessResponse, ValidationErrorResponse
from base.api.exceptions import CreateFail, UpdateFail, DeleteFail, NotFound


class CustomPagination(Pagination):
    default_limit = 20
    max_limit = 20


class SchoolYearList(generics.ListAPIView):
    serializer_class = ListSchoolYearSerializer
    pagination_class = CustomPagination
    queryset = SchoolYear.objects.all()


class SchoolYearDetail(generics.RetrieveAPIView):
    serializer_class = ListSchoolYearSerializer
    queryset = SchoolYear.objects.all()


class AddSchoolYear(views.APIView):
    permission_class = []

    def post(self, request, format=None):
        data = request.data
        school_year = {
            'name': data.get('name'),
        }
        serializer = SchoolYearSerializer(data=school_year)
        if not serializer.is_valid():
            return ValidationErrorResponse(data=serializer.data)
        try:
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Exception:
            raise CreateFail


class EditSchoolYear(generics.UpdateAPIView):
    permission_class = []

    def get_object(self):
        try:
            return SchoolYear.objects.get(id=self.kwargs["pk"])
        except SchoolYear.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if not instance:
                raise NotFound
            data = request.data
            school_year = {
                'name': data.get('name'),
            }
            serializer = SchoolYearSerializer(instance, data=school_year)
            if not serializer.is_valid():
                return ValidationErrorResponse(data=serializer.errors)
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Exception:
            raise UpdateFail


class DeleteSchoolYear(generics.DestroyAPIView):
    permission_class = []

    def get_object(self):
        try:
            return SchoolYear.objects.get(id=self.kwargs['pk'])
        except SchoolYear.DoesNotExist:
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









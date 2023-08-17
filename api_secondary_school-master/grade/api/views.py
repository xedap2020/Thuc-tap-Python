from rest_framework import generics
from rest_framework import views
from base.api.pagination import Pagination
from ..models import Grade
from .serializers import GradeSerializer, ListGradeSerializer
from base.api.response import SuccessResponse, ValidationErrorResponse
from base.api.exceptions import CreateFail, UpdateFail, DeleteFail, NotFound


class CustomPagination(Pagination):
    default_limit = 20
    max_limit = 20


class GradeList(generics.ListAPIView):
    serializer_class = ListGradeSerializer
    pagination_class = CustomPagination
    queryset = Grade.objects.all()


class GradeDetail(generics.RetrieveAPIView):
    serializer_class = ListGradeSerializer
    queryset = Grade.objects.all()


class AddGrade(views.APIView):
    permission_class = []

    def post(self, request, format=None):
        data = request.data
        grades = {
            'name': data.get('name'),
            'no': data.get('no'),
        }
        serializer = GradeSerializer(data=grades)
        if not serializer.is_valid():
            return ValidationErrorResponse(data=serializer.data)
        try:
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Exception:
            raise CreateFail


class EditGrade(generics.UpdateAPIView):
    permission_class = []

    def get_object(self):
        try:
            return Grade.objects.get(id=self.kwargs["pk"])
        except Grade.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if not instance:
                raise NotFound
            data = request.data
            grade = {
                'name': data.get('name'),
                'no': data.get('no'),
            }
            serializer = GradeSerializer(instance, data=grade)
            if not serializer.is_valid():
                return ValidationErrorResponse(data=serializer.errors)
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Exception:
            raise UpdateFail


class DeleteGrade(generics.DestroyAPIView):
    permission_class = []

    def get_object(self):
        try:
            return Grade.objects.get(id=self.kwargs['pk'])
        except Grade.DoesNotExist:
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









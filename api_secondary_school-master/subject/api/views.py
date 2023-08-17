from rest_framework import generics
from rest_framework import views
from base.api.pagination import Pagination
from ..models import Subject
from .serializers import SubjectSerializer, ListSubjectSerializer
from base.api.response import SuccessResponse, ValidationErrorResponse
from base.api.exceptions import CreateFail, UpdateFail, DeleteFail, NotFound


class CustomPagination(Pagination):
    default_limit = 20
    max_limit = 20


class SubjectList(generics.ListAPIView):
    serializer_class = ListSubjectSerializer
    pagination_class = CustomPagination
    queryset = Subject.objects.all()


class SubjectDetail(generics.RetrieveAPIView):
    serializer_class = ListSubjectSerializer
    queryset = Subject.objects.all()


class AddSubject(views.APIView):
    permission_class = []

    def post(self, request, format=None):
        data = request.data
        subject = {
            'name': data.get('name'),
            'no': data.get('no'),
        }
        serializer = SubjectSerializer(data=subject)
        if not serializer.is_valid():
            return ValidationErrorResponse(data=serializer.data)
        try:
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Exception:
            raise CreateFail


class EditSubject(generics.UpdateAPIView):
    permission_class = []

    def get_object(self):
        try:
            return Subject.objects.get(id=self.kwargs["pk"])
        except Subject.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if not instance:
                raise NotFound
            data = request.data
            subject = {
                'name': data.get('name'),
                'no': data.get('no'),
            }
            serializer = SubjectSerializer(instance, data=subject)
            if not serializer.is_valid():
                return ValidationErrorResponse(data=serializer.errors)
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Exception:
            raise UpdateFail


class DeleteSubject(generics.DestroyAPIView):
    permission_class = []

    def get_object(self):
        try:
            return Subject.objects.get(id=self.kwargs['pk'])
        except Subject.DoesNotExist:
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









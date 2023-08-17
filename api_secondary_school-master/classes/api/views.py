from rest_framework import generics, views
from base.api.pagination import Pagination
from ..models import Classes
from .serializers import ClassesSerializer, ListClassesSerializer, DetailClassesSerializer
from base.api.response import SuccessResponse, ValidationErrorResponse
from base.api.exceptions import CreateFail, UpdateFail, DeleteFail, NotFound, BadRequest
from grade.models import Grade
from rest_framework.exceptions import APIException
from rest_framework.response import Response

class CustomPagination(Pagination):
    default_limit = 20
    max_limit = 100


class ClassesList(generics.ListAPIView):
    queryset = Classes.objects.prefetch_related('grade').order_by('-created_at')
    serializer_class = ListClassesSerializer
    pagination_class = CustomPagination


class ClassesDetail(generics.RetrieveAPIView):
    serializer_class = ListClassesSerializer
    queryset = Classes.objects.all()


class AddClasses(views.APIView):
    permission_class = []

    def post(self, request, format=None):
        try:
            instance = {
            "grade": request.data.get("grade_id"),
            "name": request.data.get("name"),
            "slug": request.data.get("slug"),
            "description": request.data.get("description"),
            }
            if not instance['grade']:
                return Response({'detail': 'Invalid parameters'}, status=400)
            find_grade = Grade.objects.get(id=instance['grade'])
            if not find_grade:
                raise Grade.DoesNotExist
            serializer = ClassesSerializer(data=instance)
            if not serializer.is_valid():
                return ValidationErrorResponse(data=serializer.data)
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Grade.DoesNotExist:
            return Response({'detail': 'grade_id is invalid'}, status=400)
        except Exception as e:
            return Response({'detail': str(e)}, status=500)


class EditClasses(generics.UpdateAPIView):
    permission_class = []

    def get_object(self):
        try:
            return Classes.objects.get(id=self.kwargs["pk"])
        except Classes.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if not instance:
                raise NotFound
            update_data = {
                "grade": request.data.get("grade_id"),
                "name": request.data.get("name"),
                "slug": request.data.get("slug"),
                "description": request.data.get("description"),
            }
            if update_data['grade']:
                find_grade = Grade.objects.get(id=update_data['grade'])
                if not find_grade:
                    raise Grade.DoesNotExist
            serializer = ClassesSerializer(instance, data=update_data)
            if not serializer.is_valid():
                return ValidationErrorResponse(data=serializer.errors)
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Grade.DoesNotExist:
            return Response({'detail': 'grade_id is invalid'}, status=400)
        except Exception:
            raise UpdateFail


class DeleteClasses(generics.DestroyAPIView):
    permission_class = []

    def get_object(self):
        try:
            return Classes.objects.get(id=self.kwargs['pk'])
        except Classes.DoesNotExist:
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









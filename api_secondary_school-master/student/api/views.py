from rest_framework import generics
from rest_framework import views
from base.api.pagination import Pagination
from base.api.response import SuccessResponse, ValidationErrorResponse, Response
from base.api.exceptions import CreateFail, UpdateFail, DeleteFail, NotFound
from ..models import Student
from .serializers import StudentSerializer, ListStudentSerializer, StudentCreateSerializer
from classes.models import Classes
from school_year.models import SchoolYear

class StudentList(generics.ListAPIView):
    serializer_class = ListStudentSerializer
    pagination_class = Pagination
    queryset = Student.objects.order_by('-created_at')


class StudentDetail(generics.RetrieveAPIView):
    serializer_class = ListStudentSerializer
    queryset = Student.objects.all()


class AddStudent(views.APIView):
    permission_class = []

    def post(self, request, format=None):
        try:
            data = request.data
            student = {
                'full_name': data.get('full_name'),
                'gender': data.get('gender'),
                'birthday': data.get('birthday'),
                'address': data.get('address'),
                'nation': data.get('nation'),
                'religion': data.get('religion'),
                'father_name': data.get('father_name'),
                'father_job': data.get('father_job'),
                'mother_name': data.get('mother_name'),
                'mother_job': data.get('mother_job'),
                'classes': data.get('class_id'),
                'school_year': data.get('school_year_id'),
            }
            if not student['full_name'] or not student['gender'] or not student['birthday'] or not student['classes'] or not student['school_year']:
                return Response({'detail': 'Invalid parameters'}, status=400)
            if student['classes']:
                find_class = Classes.objects.get(id=student['classes'])
                if not find_class:
                    raise Classes.DoesNotExist
            if student['school_year']:
                find_school_year = SchoolYear.objects.get(id=student['school_year'])
                if not find_school_year:
                    raise SchoolYear.DoesNotExist
            serializer = StudentCreateSerializer(data=student)
            if not serializer.is_valid():
                return ValidationErrorResponse(data=serializer.data)
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Classes.DoesNotExist:
            return Response({'detail': 'class_id is invalid'}, status=400)
        except SchoolYear.DoesNotExist:
            return Response({'detail': 'school_year_id is invalid'}, status=400)
        except Exception:
            raise CreateFail


class EditStudent(generics.UpdateAPIView):
    permission_class = []

    def get_object(self):
        try:
            return Student.objects.get(id=self.kwargs["pk"])
        except Student.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if not instance:
                raise NotFound
                
            data = request.data
            student = {
                'full_name': data.get('full_name'),
                'gender': data.get('gender'),
                'birthday': data.get('birthday'),
                'address': data.get('address'),
                'nation': data.get('nation'),
                'religion': data.get('religion'),
                'father_name': data.get('father_name'),
                'father_job': data.get('father_job'),
                'mother_name': data.get('mother_name'),
                'mother_job': data.get('mother_job'),
                'classes': data.get('class_id'),
                'school_year': data.get('school_year_id'),
            }
            if student['classes']:
                find_class = Classes.objects.get(id=student['classes'])
                if not find_class:
                    raise Classes.DoesNotExist
            if student['school_year']:
                find_school_year = SchoolYear.objects.get(id=student['school_year'])
                if not find_school_year:
                    raise SchoolYear.DoesNotExist
            serializer = StudentSerializer(instance, data=student)
            if not serializer.is_valid():
                return ValidationErrorResponse(data=serializer.errors)
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Classes.DoesNotExist:
            return Response({'detail': 'class_id is invalid'}, status=400)
        except SchoolYear.DoesNotExist:
            return Response({'detail': 'school_year_id is invalid'}, status=400)
        except Exception:
            raise UpdateFail


class DeleteStudent(generics.DestroyAPIView):
    permission_class = []

    def get_object(self):
        try:
            return Student.objects.get(id=self.kwargs['pk'])
        except Student.DoesNotExist:
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

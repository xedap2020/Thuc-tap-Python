from rest_framework import generics
from rest_framework import views
from base.api.pagination import Pagination
from base.api.response import SuccessResponse, ValidationErrorResponse, ErrorResponse
from base.api.exceptions import CreateFail, UpdateFail, DeleteFail, NotFound
from ..models import ClassSubject
from classes.models import Classes
from subject.models import Subject
from school_year.models import SchoolYear
from user.models import User
from .serializers import ClassSubjectsSerializer, ListClassSubjectsSerializer, ClassCreateSubjectsSerializer


class ClassSubjectList(generics.ListAPIView):
    serializer_class = ListClassSubjectsSerializer
    pagination_class = Pagination
    queryset = ClassSubject.objects.prefetch_related('classes', 'subject').order_by('-created_at')


class ClassSubjectDetail(generics.RetrieveAPIView):
    serializer_class = ClassSubjectsSerializer
    queryset = ClassSubject.objects.all()


class AddClassSubject(views.APIView):
    permission_class = []

    def post(self, request, format=None):
        data = request.data

        find_class = Classes.objects.filter(pk=data.get('class_id')).first()
        if not find_class:
            return ErrorResponse(status=400, message="Class does not exist")

        find_subject = Subject.objects.filter(pk=data.get('subject_id')).first()
        if not find_subject:
            return ErrorResponse(status=400, message="Subject does not exist")

        find_school_year = SchoolYear.objects.filter(pk=data.get('school_year_id')).first()
        if not find_school_year:
            return ErrorResponse(status=400, message="School year does not exist")

        find_teacher = User.objects.filter(pk=data.get('user_id')).filter(position='Giáo viên').first()
        if not find_teacher:
            return ErrorResponse(status=400, message="Teacher does not exist")
    
        check_exist = ClassSubject.objects.filter(classes=find_class).filter(subject=find_subject).filter(school_year=find_school_year).filter(user=find_teacher).first()
        if check_exist:
            return ErrorResponse(status=400, message="Class - Subject - School year and Teacher are exist")
        
        serializer = ClassCreateSubjectsSerializer(data={
            "classes": find_class.id,
            "subject": find_subject.id,
            "user": find_teacher.id,
            "school_year": find_school_year.id,
            "can_teach_section_1": data.get('can_teach_section_1'),
            "can_teach_section_2": data.get('can_teach_section_2'),
        })

        if not serializer.is_valid():
            return ValidationErrorResponse(data=serializer.data)
        try:
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Exception:
            raise CreateFail


class DeleteClassSubject(generics.DestroyAPIView):
    permission_class = []

    def get_object(self):
        try:
            return ClassSubject.objects.get(id=self.kwargs['pk'])
        except ClassSubject.DoesNotExist:
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









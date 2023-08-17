from rest_framework import generics
from rest_framework import views
from base.api.pagination import Pagination
from base.api.response import SuccessResponse, ValidationErrorResponse, Response, ErrorResponse
from base.api.exceptions import CreateFail, UpdateFail, DeleteFail, NotFound
from ..models import Point, Performance
from .serializers import PointSerializer, PointUpdateSerializer, ListPointSerializer, PointCreateSerializer, PerformanceCreateSerializer, PerformanceSerializer, ListPerformanceSerializer, PerformanceSerializer
from student.models import Student
from class_subject.models import ClassSubject
from django.db.models import Count

class PointList(generics.ListAPIView):
    serializer_class = ListPointSerializer
    pagination_class = Pagination
    queryset = Point.objects.order_by('-created_at')


class PointDetail(generics.RetrieveAPIView):
    serializer_class = ListPointSerializer
    queryset = Point.objects.all()


class PointView(views.APIView):
    permission_class = []

    def get_object(self):
        try:
            return Point.objects.get(id=self.kwargs["pk"])
        except Point.DoesNotExist:
            return None

    def avg_point_calculator(self, point):
        avg_15 = (point['exam_15_no_1'] + point['exam_15_no_2'] + point['exam_15_no_3'] + point['exam_15_no_4']) / 4 
        avg_45 = (point['exam_45_no_1'] + point['exam_45_no_2']) / 2
        avg_kt = (point['exam_quick'] + avg_15 + 2 * avg_45) / 4
        point['avg_point'] = round((avg_kt * 2 + point['exam_finally']) / 3, 2)
        return point

    def extract_data(self, data):
        point = {
            'student': data.get('student_id'),
            'class_subject': data.get('class_subject_id'),
            'exam_quick': data.get('exam_quick') if data.get('exam_quick') else 0,
            'exam_15_no_1': data.get('exam_15_no_1') if data.get('exam_15_no_1') else 0,
            'exam_15_no_2': data.get('exam_15_no_2') if data.get('exam_15_no_2') else 0,
            'exam_15_no_3': data.get('exam_15_no_3') if data.get('exam_15_no_3') else 0,
            'exam_15_no_4': data.get('exam_15_no_4') if data.get('exam_15_no_4') else 0,
            'exam_45_no_1': data.get('exam_45_no_1') if data.get('exam_45_no_1') else 0,
            'exam_45_no_2': data.get('exam_45_no_2') if data.get('exam_45_no_2') else 0,
            'exam_finally': data.get('exam_finally') if data.get('exam_finally') else 0,
            'is_section_1': data.get('is_section_1') if data.get('exam_quick') else False,
            'is_section_2': data.get('is_section_2') if data.get('exam_quick') else False,
        }
        point = self.avg_point_calculator(point)
        return point

    def fill_performance(self, performance):
        performance['conduct_classification_section_1'] = None
        performance['conduct_classification_section_2'] = None
        performance['conduct_classification_overall'] = None
        performance['positive_section_1'] = None
        performance['positive_section_2'] = None
        performance['negative_section_1'] = None
        performance['negative_section_2'] = None
        performance['days_off_section_1'] = 0
        performance['days_off_section_2'] = 0
        performance['days_off_overall'] = 0
        performance['rank_section_1'] = None
        performance['rank_section_2'] = None
        performance['rank_overall'] = None
        performance['note_overall'] = None
        return performance
    
    # Tính điểm tổng kết
    def sync_performance(self, student, class_subject):
        try:
            # Tổng số môn học
            s_id = student.id
            s_y_id = student.school_year_id
            class_id = student.classes_id
            if s_y_id is not class_subject.school_year_id:
                return ErrorResponse(status=400, message="School year is invalid")

            qs = ClassSubject.objects.filter(school_year_id=s_y_id, classes_id=class_id)

            class_subjects = []
            for item in qs:
                class_subjects.append(item.id)
            print("class_subjects = ", class_subjects)

            qs = qs.values('subject_id').distinct()
            subjects = []
            for item in qs:
                subjects.append(item['subject_id'])
            print("subjects = ", subjects)

            total_subjects = qs.count()

            # Điểm trung bình của kì 1 và kì 2
            total_score_section_1 = 0
            total_score_section_2 = 0

            qs_student_points = Point.objects.filter(student_id=s_id, class_subject_id__in=class_subjects)
            for item in qs_student_points:
                if item.is_section_1:
                    total_score_section_1 += item.avg_point
                if item.is_section_2:
                    total_score_section_2 += item.avg_point
        
            medium_score_section_1 = round(total_score_section_1/total_subjects, 2)
            medium_score_section_2 = round(total_score_section_2/total_subjects, 2)
            medium_score_overall = round((total_score_section_1/total_subjects + 2*total_score_section_2/total_subjects)/3, 2)

            print("medium_score_section_1 = ", medium_score_section_1)
            print("medium_score_section_2 = ", medium_score_section_2)
            print("medium_score_overall = ", medium_score_overall)
            performance = self.fill_performance({
                'school_year': s_y_id,
                'classes': class_subject.classes_id,
                'student': s_id,
                'teacher': class_subject.user_id,
                'medium_score_section_1': medium_score_section_1,
                'medium_score_section_2': medium_score_section_2,
                'medium_score_overall': medium_score_overall,
            })

            find_performance = Performance.objects.filter(school_year_id=s_y_id, student=student).first()
            if not find_performance:
                print("Create new performance")
                performance_serializer = PerformanceCreateSerializer(data=performance)
                if not performance_serializer.is_valid():
                    return ValidationErrorResponse(data=performance_serializer.data)
                performance_serializer.save()
            else:
                print("Update performance")
                performance_serializer = PerformanceSerializer(find_performance, data=performance)
                if not performance_serializer.is_valid():
                    return ValidationErrorResponse(data=serializer.errors)
                performance_serializer.save()

        except Exception:
            return ErrorResponse(status=500, message="Internal Server Error")

    def post(self, request, format=None):
        try:
            point = self.extract_data(request.data)
            if not point['student'] or not point['class_subject'] or (point['is_section_1'] is point['is_section_2']):
                return Response({'detail': 'Invalid parameters'}, status=400)

            find_student = Student.objects.filter(id=point['student']).first()
            if not find_student:
                return ErrorResponse(status=400, message="Student does not exist")

            find_class_subject = ClassSubject.objects.filter(id=point['class_subject']).first()
            if not find_class_subject:
                return ErrorResponse(status=400, message="Class subject does not exist")

            # TODO::năm học của học sinh và vào điểm đã khớp hay chưa 
            # TODO::validate teacher enter points for students

            find_point = Point.objects.filter(is_section_1=point['is_section_1'], \
            is_section_2=point['is_section_2'], class_subject=find_class_subject, student=find_student).first()

            if find_point:
                return ErrorResponse(status=400, message="Point does exist")

            serializer = PointCreateSerializer(data=point)

            if not serializer.is_valid():
                return ValidationErrorResponse(data=serializer.data)
            serializer.save()

            self.sync_performance(find_student, find_class_subject)

            return SuccessResponse(data=serializer.data)
        except Exception:
            return ErrorResponse(status=500, message="Internal Server Error")

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if not instance:
                raise NotFound
                
            point = self.extract_data(request.data)
            if instance.class_subject_id is not point['class_subject']:
                return Response({'detail': 'Invalid parameters'}, status=400)

            find_student = Student.objects.filter(id=point['student']).first()
            if not find_student:
                return ErrorResponse(status=400, message="Student does not exist")

            find_class_subject = ClassSubject.objects.filter(id=point['class_subject']).first()
            if not find_class_subject:
                return ErrorResponse(status=400, message="Class subject does not exist")
            
            serializer = PointUpdateSerializer(instance, data=point)
            if not serializer.is_valid():
                return ValidationErrorResponse(data=serializer.errors)

            serializer.save()

            self.sync_performance(find_student, find_class_subject)

            return SuccessResponse(data=serializer.data)
        except Exception:
            return ErrorResponse(status=500, message="Internal Server Error")

    def delete(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
            if not obj:
                raise NotFound
            print("obj = ", obj.id)
            find_student = Student.objects.filter(id=obj.student_id).first()
            if not find_student:
                return ErrorResponse(status=400, message="Student does not exist")

            find_class_subject = ClassSubject.objects.filter(id=obj.class_subject_id).first()
            if not find_class_subject:
                return ErrorResponse(status=400, message="Class subject does not exist")

            obj.delete()

            self.sync_performance(find_student, find_class_subject)

            return SuccessResponse(message='Delete success')
        except Exception:
            return ErrorResponse(status=500, message="Internal Server Error")

class PerformanceList(generics.ListAPIView):
    serializer_class = ListPerformanceSerializer
    pagination_class = Pagination
    queryset = Performance.objects.order_by('-created_at')

class EditPerformance(generics.UpdateAPIView):
    permission_class = []

    def get_object(self):
        try:
            return Performance.objects.get(id=self.kwargs["pk"])
        except Performance.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if not instance:
                raise NotFound
                
            data = request.data
            point = {
                'school_year': data.get('school_year_id'),
                'classes': data.get('classes_id'),
                'teacher': data.get('teacher_id'),

                'conduct_classification_section_1': data.get('conduct_classification_section_1'),
                'conduct_classification_section_2': data.get('conduct_classification_section_2'),
                'conduct_classification_overall': data.get('conduct_classification_overall'),
                'positive_section_1': data.get('positive_section_1'),
                'positive_section_2': data.get('positive_section_2'),
                'negative_section_1': data.get('negative_section_1'),
                'negative_section_2': data.get('negative_section_2'),
                'days_off_section_1': data.get('days_off_section_1'),
                'days_off_section_2': data.get('days_off_section_2'),
                'days_off_overall': data.get('days_off_overall'),
                'rank_section_1': data.get('rank_section_1'),
                'rank_section_2': data.get('rank_section_2'),
                'rank_overall': data.get('rank_overall'),
                'note_overall': data.get('note_overall'),
            }

            serializer = PerformanceSerializer(instance, data=point)

            if not serializer.is_valid():
                return ValidationErrorResponse(data=serializer.errors)
            serializer.save()
            return SuccessResponse(data=serializer.data)
        except Exception:
            return ErrorResponse(status=500, message="Internal Server Error")

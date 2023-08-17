from django.db import models
from student.models import Student
from class_subject.models import ClassSubject
from classes.models import Classes
from user.models import User
from school_year.models import SchoolYear

class Point(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Học sinh"
    )
    class_subject = models.ForeignKey(
        ClassSubject,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Lớp - môn học - giáo viên - năm học - kì học"
    )
    exam_quick = models.FloatField(default=0, verbose_name='Kiểm tra miệng')
    exam_15_no_1 = models.FloatField(default=0, verbose_name='Kiểm tra 15 phút lần 1')
    exam_15_no_2 = models.FloatField(default=0, verbose_name='Kiểm tra 15 phút lần 2')
    exam_15_no_3 = models.FloatField(default=0, verbose_name='Kiểm tra 15 phút lần 3')
    exam_15_no_4 = models.FloatField(default=0, verbose_name='Kiểm tra 15 phút lần 4')
    exam_45_no_1 = models.FloatField(default=0, verbose_name='Kiểm tra 1 tiết lần 1')
    exam_45_no_2 = models.FloatField(default=0, verbose_name='Kiểm tra 1 tiết lần 2')
    exam_finally = models.FloatField(default=0, verbose_name='Kiểm tra cuối kì')
    avg_point = models.FloatField(default=0, verbose_name='Trung bình môn')
    is_section_1 = models.BooleanField(default=False, verbose_name="Học kỳ I")
    is_section_2 = models.BooleanField(default=False, verbose_name="Học kỳ II")
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày cập nhật")

    class Meta:
        db_table = 'points'
        verbose_name = "Điểm"
        verbose_name_plural = "Điểm"


class Performance(models.Model):
    school_year = models.ForeignKey(
        SchoolYear,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Năm học"
    )
    classes = models.ForeignKey(
        Classes,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Lớp học"
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Học sinh"
    )
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Giáo viên chủ nhiệm"
    )
    medium_score_section_1 = models.FloatField(default=0, verbose_name='Điểm tổng kết HK I')
    medium_score_section_2 = models.FloatField(default=0, verbose_name='Điểm tổng kết HK II')
    medium_score_overall = models.FloatField(default=0, verbose_name='Điểm tổng kết cả năm học')

    conduct_classification_section_1 = models.CharField(max_length=10, blank=True, null=True, verbose_name="Xếp loại hạnh kiểm HK I")
    conduct_classification_section_2 = models.CharField(max_length=10, blank=True, null=True, verbose_name="Xếp loại hạnh kiểm HK II")
    conduct_classification_overall = models.CharField(max_length=10, blank=True, null=True, verbose_name="Xếp loại hạnh kiểm cả năm")

    positive_section_1 = models.CharField(max_length=500, blank=True, null=True, verbose_name="Điểm tốt học kì I") # Khen thưởng,...
    positive_section_2 = models.CharField(max_length=500, blank=True, null=True, verbose_name="Điểm tốt học kì II")
    negative_section_1 = models.CharField(max_length=500, blank=True, null=True, verbose_name="Điểm chưa tốt học kì I") # Kỉ luật,... 
    negative_section_2 = models.CharField(max_length=500, blank=True, null=True, verbose_name="Điểm chưa tốt học kì II")

    days_off_section_1 = models.FloatField(default=0, verbose_name='Số ngày nghỉ học HK I')
    days_off_section_2 = models.FloatField(default=0, verbose_name='Số ngày nghỉ học HK II')
    days_off_overall = models.FloatField(default=0, verbose_name='Số ngày nghỉ học cả năm học')

    rank_section_1 = models.CharField(max_length=10, blank=True, null=True, verbose_name="Học lực HK I")
    rank_section_2 = models.CharField(max_length=10, blank=True, null=True, verbose_name="Học lực HK II")
    rank_overall = models.CharField(max_length=10, blank=True, null=True, verbose_name="Học lực cả năm")

    note_overall = models.CharField(max_length=500, blank=True, null=True, verbose_name="Đánh giá chung của giáo viên")

    created_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày cập nhật")

    class Meta:
        db_table = 'performances'
        verbose_name = "Tổng kết"
        verbose_name_plural = "Tổng kết"
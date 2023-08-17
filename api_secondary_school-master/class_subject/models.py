from django.db import models
from classes.models import Classes
from subject.models import Subject
from user.models import User
from school_year.models import SchoolYear

class ClassSubject(models.Model):
    classes = models.ForeignKey(
        Classes,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Lớp học"
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Môn học"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Giáo viên"
    )
    school_year = models.ForeignKey(
        SchoolYear,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Năm học"
    )
    can_teach_section_1 = models.BooleanField(default=True, verbose_name="Học kỳ I")
    can_teach_section_2 = models.BooleanField(default=True, verbose_name="Học kỳ II")
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày cập nhật")

    def __str__(self):
        return 'Class : {}, subject : {}'.format(self.classes, self.subject)

    class Meta:
        db_table = 'class_subjects'
        verbose_name = "Lớp học môn học"
        verbose_name_plural = "Lớp học môn học"




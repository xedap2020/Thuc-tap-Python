from django.db import models
from classes.models import Classes
from school_year.models import SchoolYear

class Student(models.Model):
    full_name = models.CharField(max_length=50, blank=False, null=False, verbose_name="Tên đầy đủ")
    gender = models.CharField(max_length=4, null=True, blank=True, verbose_name="Giới tính")
    birthday = models.DateField(auto_now=False, blank=True, null=True, verbose_name="Ngày tháng năm sinh")
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nơi sinh")
    nation = models.CharField(max_length=100, blank=True, null=True, verbose_name="Dân tộc")
    religion = models.CharField(max_length=10, null=True, blank=True, verbose_name="Tôn giáo")
    father_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tên bố")
    father_job = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nghề nghiêp bố")
    mother_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tên mẹ")
    mother_job = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nghề nghiêp mẹ")

    school_year = models.ForeignKey(
        SchoolYear,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Năm học"
    )
    classes = models.ForeignKey(
        Classes,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Lớp"
    )
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày cập nhật")

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'students'
        verbose_name = "Học sinh"
        verbose_name_plural = "Học sinh"
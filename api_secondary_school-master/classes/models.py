from django.db import models
from grade.models import Grade

class Classes(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, verbose_name="Tên khóa học")
    slug = models.SlugField(blank=False, null=False)
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mô tả")
    grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Khối"
    )
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày cập nhật")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'classes'
        verbose_name = "Lớp học"
        verbose_name_plural = "Lớp học"




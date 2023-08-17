from django.db import models
from django.template.defaultfilters import slugify


class SchoolYear(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, verbose_name="Năm học")
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày cập nhật")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'school_years'
        verbose_name = "Năm học"
        verbose_name_plural = "Năm học"




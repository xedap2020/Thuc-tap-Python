from django.db import models
from department.models import Department

class User(models.Model):
    full_name = models.CharField(max_length=200, blank=False, null=False, verbose_name="Tên đầy đủ")
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name="Số điện thoại")
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name="Email")
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name="Địa chỉ")
    specialize = models.CharField(max_length=500, null=True, blank=True, verbose_name="Chuyên môn")
    position = models.CharField(max_length=500, null=True, blank=True, verbose_name="Chức vụ")
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày cập nhật")
    password = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mật khẩu")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Tổ"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'users'
        verbose_name = "Người dùng"
        verbose_name_plural = "Người dùng"
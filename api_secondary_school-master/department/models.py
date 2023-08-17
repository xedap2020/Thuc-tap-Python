from django.db import models
from django.template.defaultfilters import slugify


class Department(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, verbose_name="Tổ")
    slug = models.SlugField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày cập nhật")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)

    class Meta:
        db_table = 'departments'
        verbose_name = "Tổ"
        verbose_name_plural = "Tổ"




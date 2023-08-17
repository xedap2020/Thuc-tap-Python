from django.db import models
from django.template.defaultfilters import slugify


class Subject(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, verbose_name="Môn học")
    slug = models.SlugField(blank=False, null=False)
    no = models.IntegerField(blank=True, null=True, verbose_name='Số')
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Ngày cập nhật")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)

    class Meta:
        db_table = 'subjects'
        verbose_name = "Môn học"
        verbose_name_plural = "Môn học"




# Generated by Django 4.2.4 on 2023-08-12 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Tên khóa học')),
                ('slug', models.SlugField()),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mô tả')),
                ('created_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Ngày cập nhật')),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grade.grade', verbose_name='Khối')),
            ],
            options={
                'verbose_name': 'Lớp học',
                'verbose_name_plural': 'Lớp học',
                'db_table': 'classes',
            },
        ),
    ]

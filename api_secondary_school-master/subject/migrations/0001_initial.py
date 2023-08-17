# Generated by Django 4.2.4 on 2023-08-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Môn học')),
                ('slug', models.SlugField()),
                ('no', models.IntegerField(blank=True, null=True, verbose_name='Số')),
                ('created_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Ngày cập nhật')),
            ],
            options={
                'verbose_name': 'Môn học',
                'verbose_name_plural': 'Môn học',
                'db_table': 'subjects',
            },
        ),
    ]

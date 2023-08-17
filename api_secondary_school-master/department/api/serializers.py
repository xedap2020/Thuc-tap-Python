from rest_framework import serializers
from ..models import Department
from django.template.defaultfilters import slugify


class ListDepartmentSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = [
            'id',
            'name',
            'slug',
            'created_at',
            'updated_at'
        ]

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_updated_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = [
            'id',
            'name',
        ]

    def create(self, validated_data):
        department = Department.objects.create(**validated_data)
        return department

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.slug = slugify(validated_data.get("name", instance.name))
        instance.save()
        return instance







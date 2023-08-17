from rest_framework import serializers
from ..models import Classes
from grade.models import Grade

class ListClassesSerializer(serializers.ModelSerializer):
    grade = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Classes
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'grade',
            'created_at',
            'updated_at',
        ]

    def get_grade(self, obj):
        if not obj.grade:
            return None
        return {'id': getattr(obj.grade, 'id'), 'name': getattr(obj.grade, 'name'), 'slug': getattr(obj.grade, 'slug')}

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_updated_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_description(self, obj):
        if not obj.description:
            return None
        return obj.description


class DetailClassesSerializer(serializers.ModelSerializer):
    grade = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Classes
        fields = [
            'name',
            'slug',
            'description',
            'grade',
            'created_at',
            'updated_at',
        ]

    def get_grade(self, obj):
        if not obj.grade:
            return None
        return {'id': getattr(obj.grade, 'id'), 'name': getattr(obj.grade, 'name'), 'slug': getattr(obj.grade, 'slug')}
        
    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_updated_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None


class ClassesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classes
        fields = [
            'grade',
            'name',
            'slug',
            'description',
        ]

    def create(self, validated_data):
        classes = Classes.objects.create(**validated_data)
        return classes

    def update(self, instance, validated_data):
        instance.grade = validated_data.get("grade", instance.grade.id)
        instance.name = validated_data.get("name", instance.name)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance







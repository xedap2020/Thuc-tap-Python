from rest_framework import serializers
from ..models import Student


class ListStudentSerializer(serializers.ModelSerializer):
    classes = serializers.SerializerMethodField()
    school_year = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            'id',
            'full_name',
            'gender',
            'birthday',
            'address',
            'nation',
            'religion',
            'father_name',
            'father_job',
            'mother_name',
            'mother_job',
            'classes',
            'school_year',
            'created_at',
            'updated_at'
        ]

    def get_classes(self, obj):
        if not obj.classes:
            return None
        return {'id': getattr(obj.classes, 'id'), 'name': getattr(obj.classes, 'name'), 'slug': getattr(obj.classes, 'slug'), 'description': getattr(obj.classes, 'description')}
    
    def get_school_year(self, obj):
        if not obj.school_year:
            return None
        return {'id': getattr(obj.school_year, 'id'), 'name': getattr(obj.school_year, 'name')}

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_updated_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

class StudentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            'full_name',
            'gender',
            'birthday',
            'address',
            'nation',
            'religion',
            'father_name',
            'father_job',
            'mother_name',
            'mother_job',
            'classes',
            'school_year',
        ]

    def create(self, validated_data):
        student = Student.objects.create(**validated_data)
        return student

class DetailStudentSerializer(serializers.ModelSerializer):
    classes = serializers.SerializerMethodField()
    school_year = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            'full_name',
            'gender',
            'birthday',
            'address',
            'nation',
            'religion',
            'father_name',
            'father_job',
            'mother_name',
            'mother_job',
            'classes',
            'school_year',
            'created_at',
            'updated_at',
        ]

    def get_classes(self, obj):
        if not obj.classes:
            return None
        return {'id': getattr(obj.classes, 'id'), 'name': getattr(obj.classes, 'name'), 'slug': getattr(obj.classes, 'slug'), 'description': getattr(obj.classes, 'description')}
    
    def get_school_year(self, obj):
        if not obj.school_year:
            return None
        return {'id': getattr(obj.school_year, 'id'), 'name': getattr(obj.school_year, 'name')}
        
    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_updated_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            'full_name',
            'gender',
            'birthday',
            'address',
            'nation',
            'religion',
            'father_name',
            'father_job',
            'mother_name',
            'mother_job',
            'classes',
            'school_year',
        ]
    
    def update(self, instance, validated_data):
        instance.gender = validated_data.get("gender", instance.gender)
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.birthday = validated_data.get("birthday", instance.birthday)
        instance.address = validated_data.get("address", instance.address)
        instance.nation = validated_data.get("nation", instance.nation)
        instance.religion = validated_data.get("religion", instance.religion)
        instance.father_name = validated_data.get("father_name", instance.father_name)
        instance.father_job = validated_data.get("father_job", instance.father_job)
        instance.mother_name = validated_data.get("mother_name", instance.mother_name)
        instance.mother_job = validated_data.get("mother_job", instance.mother_job)
        instance.classes = validated_data.get("classes", instance.classes)
        instance.school_year = validated_data.get("school_year", instance.school_year)
        instance.save()
        return instance







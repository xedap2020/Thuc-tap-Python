from rest_framework import serializers
from ..models import ClassSubject


class ListClassSubjectsSerializer(serializers.ModelSerializer):
    classes = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    school_year = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = ClassSubject
        fields = [
            'id',
            'classes',
            'subject',
            'school_year',
            'user',
            'can_teach_section_1',
            'can_teach_section_2',
            'created_at',
            'updated_at',
        ]

    def get_classes(self, obj):
        if not obj.classes:
            return None
        return {'id': getattr(obj.classes, 'id'), 'name': getattr(obj.classes, 'name'), 'slug': getattr(obj.classes, 'slug')}

    def get_subject(self, obj):
        if not obj.subject:
            return None
        return {'id': getattr(obj.subject, 'id'), 'name': getattr(obj.subject, 'name'), 'slug': getattr(obj.subject, 'slug')}

    def get_school_year(self, obj):
        if not obj.school_year:
            return None
        return {'id': getattr(obj.school_year, 'id'), 'name': getattr(obj.school_year, 'name')}

    def get_user(self, obj):
        if not obj.user:
            return None
        return {'id': getattr(obj.user, 'id'), 'full_name': getattr(obj.user, 'full_name'), 'phone': getattr(obj.user, 'phone'), 'specialize': getattr(obj.user, 'specialize'), 'position': getattr(obj.user, 'position')}

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_updated_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

class ClassCreateSubjectsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClassSubject
        fields = [
            'classes',
            'subject',
            'school_year',
            'user',
            'can_teach_section_1',
            'can_teach_section_2',
        ]

    def create(self, validated_data):
        instance = ClassSubject.objects.create(**validated_data)
        return instance

class ClassSubjectsSerializer(serializers.ModelSerializer):
    classes = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    school_year = serializers.SerializerMethodField()

    class Meta:
        model = ClassSubject
        fields = [
            'classes',
            'subject',
            'school_year',
            'user',
            'can_teach_section_1',
            'can_teach_section_2',
        ]

    def create(self, validated_data):
        instance = ClassSubject.objects.create(**validated_data)
        return instance

    def get_classes(self, obj):
        if not obj.classes:
            return None
        return {'id': getattr(obj.classes, 'id'), 'name': getattr(obj.classes, 'name'), 'slug': getattr(obj.classes, 'slug')}

    def get_subject(self, obj):
        if not obj.subject:
            return None
        return {'id': getattr(obj.subject, 'id'), 'name': getattr(obj.subject, 'name'), 'slug': getattr(obj.subject, 'slug')}

    def get_school_year(self, obj):
        if not obj.school_year:
            return None
        return {'id': getattr(obj.school_year, 'id'), 'name': getattr(obj.school_year, 'name')}

    def get_user(self, obj):
        if not obj.user:
            return None
        return {'id': getattr(obj.user, 'id'), 'full_name': getattr(obj.user, 'full_name'), 'phone': getattr(obj.user, 'phone'), 'specialize': getattr(obj.user, 'specialize'), 'position': getattr(obj.user, 'position')}

    





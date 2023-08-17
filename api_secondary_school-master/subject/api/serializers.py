from rest_framework import serializers
from ..models import Subject
from django.template.defaultfilters import slugify


class ListSubjectSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Subject
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


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = [
            'id',
            'name',
            'no',
        ]

    def create(self, validated_data):
        subject = Subject.objects.create(**validated_data)
        return subject

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.slug = slugify(validated_data.get("name", instance.name))
        instance.no = validated_data.get("no", instance.no)
        instance.save()
        return instance







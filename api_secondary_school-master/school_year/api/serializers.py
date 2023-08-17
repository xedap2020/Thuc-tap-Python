from rest_framework import serializers
from ..models import SchoolYear

class ListSchoolYearSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = SchoolYear
        fields = [
            'id',
            'name',
            'created_at',
            'updated_at'
        ]

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_updated_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None


class SchoolYearSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolYear
        fields = [
            'id',
            'name',
        ]

    def create(self, validated_data):
        school_year = SchoolYear.objects.create(**validated_data)
        return school_year

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance







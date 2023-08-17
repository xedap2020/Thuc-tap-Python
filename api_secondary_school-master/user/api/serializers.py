from rest_framework import serializers
from ..models import User


class ListUserSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'phone',
            'email',
            'address',
            'position',
            'specialize',
            'department',
            'created_at',
            'updated_at'
        ]

    def get_department(self, obj):
        if not obj.department:
            return None
        return {'id': getattr(obj.department, 'id'), 'name': getattr(obj.department, 'name'), 'slug': getattr(obj.department, 'slug')}

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_updated_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'full_name',
            'email',
            'address',
            'phone',
            'position',
            'specialize',
            'department',
            'password',
        ]

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

class DetailUserSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'name',
            'slug',
            'description',
            'grade',
            'created_at',
            'updated_at',
            'department',
        ]

    def get_department(self, obj):
        if not obj.department:
            return None
        return {'id': getattr(obj.department, 'id'), 'name': getattr(obj.grade, 'name'), 'slug': getattr(obj.grade, 'slug')}
        
    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_updated_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'full_name',
            'email',
            'address',
            'phone',
            'position',
            'specialize',
            'department',
        ]
    
    def update(self, instance, validated_data):
        instance.department = validated_data.get("department", instance.department)
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.email = validated_data.get("email", instance.email)
        instance.position = validated_data.get("position", instance.position)
        instance.specialize = validated_data.get("specialize", instance.specialize)
        instance.save()
        return instance







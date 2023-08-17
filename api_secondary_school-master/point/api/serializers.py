from rest_framework import serializers
from ..models import Point, Performance


class ListPointSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    class_subject = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Point
        fields = [
            'id',
            'student',
            'class_subject',
            'exam_quick',
            'exam_15_no_1',
            'exam_15_no_2',
            'exam_15_no_3',
            'exam_15_no_4',
            'exam_45_no_1',
            'exam_45_no_2',
            'exam_finally',
            'avg_point',
            'is_section_1',
            'is_section_2',
            'created_at',
            'updated_at'
        ]

    def get_student(self, obj):
        if not obj.student:
            return None
        return {'id': getattr(obj.student, 'id'), 'name': getattr(obj.student, 'name')}

    def get_class_subject(self, obj):
        if not obj.class_subject:
            return None
        return {'id': getattr(obj.student, 'id')}

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_updated_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

class PointCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = [
            'student',
            'class_subject',
            'exam_quick',
            'exam_15_no_1',
            'exam_15_no_2',
            'exam_15_no_3',
            'exam_15_no_4',
            'exam_45_no_1',
            'exam_45_no_2',
            'exam_finally',
            'avg_point',
            'is_section_1',
            'is_section_2',
        ]

    def create(self, validated_data):
        point = Point.objects.create(**validated_data)
        return point

class DetailPointSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    class_subject = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Point
        fields = [
            'student',
            'class_subject',
            'exam_quick',
            'exam_15_no_1',
            'exam_15_no_2',
            'exam_15_no_3',
            'exam_15_no_4',
            'exam_45_no_1',
            'exam_45_no_2',
            'exam_finally',
            'avg_point',
            'is_section_1',
            'is_section_2',
            'created_at',
            'updated_at'
        ]

    def get_student(self, obj):
        if not obj.student:
            return None
        return {'id': getattr(obj.student, 'id'), 'name': getattr(obj.student, 'name')}

    def get_class_subject(self, obj):
        if not obj.class_subject:
            return None
        return {'id': getattr(obj.student, 'id')}

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_updated_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None


class PointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = [
            'student',
            'class_subject',
            'exam_quick',
            'exam_15_no_1',
            'exam_15_no_2',
            'exam_15_no_3',
            'exam_15_no_4',
            'exam_45_no_1',
            'exam_45_no_2',
            'exam_finally',
            'avg_point',
            'is_section_1',
            'is_section_2',
            'created_at',
            'updated_at'
        ]
    
    def update(self, instance, validated_data):
        instance.student = validated_data.get("student", instance.student)
        instance.class_subject = validated_data.get("class_subject", instance.class_subject)
        instance.exam_quick = validated_data.get("exam_quick", instance.exam_quick)
        instance.exam_15_no_1 = validated_data.get("exam_15_no_1", instance.exam_15_no_1)
        instance.exam_15_no_2 = validated_data.get("exam_15_no_2", instance.exam_15_no_2)
        instance.exam_15_no_3 = validated_data.get("exam_15_no_3", instance.exam_15_no_3)
        instance.exam_15_no_4 = validated_data.get("exam_15_no_4", instance.exam_15_no_4)
        instance.exam_45_no_1 = validated_data.get("exam_45_no_1", instance.exam_45_no_1)
        instance.exam_45_no_2 = validated_data.get("exam_45_no_2", instance.exam_45_no_2)
        instance.exam_finally = validated_data.get("exam_finally", instance.exam_finally)
        instance.is_section_1 = validated_data.get("is_section_1", instance.is_section_1)
        instance.is_section_2 = validated_data.get("is_section_2", instance.is_section_2)
        instance.save()
        return instance

class PointUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = [
            'student',
            'class_subject',
            'exam_quick',
            'exam_15_no_1',
            'exam_15_no_2',
            'exam_15_no_3',
            'exam_15_no_4',
            'exam_45_no_1',
            'exam_45_no_2',
            'exam_finally',
            'avg_point',
        ]
    
    def update(self, instance, validated_data):
        instance.student = validated_data.get("student", instance.student)
        instance.class_subject = validated_data.get("class_subject", instance.class_subject)
        instance.exam_quick = validated_data.get("exam_quick", instance.exam_quick)
        instance.exam_15_no_1 = validated_data.get("exam_15_no_1", instance.exam_15_no_1)
        instance.exam_15_no_2 = validated_data.get("exam_15_no_2", instance.exam_15_no_2)
        instance.exam_15_no_3 = validated_data.get("exam_15_no_3", instance.exam_15_no_3)
        instance.exam_15_no_4 = validated_data.get("exam_15_no_4", instance.exam_15_no_4)
        instance.exam_45_no_1 = validated_data.get("exam_45_no_1", instance.exam_45_no_1)
        instance.exam_45_no_2 = validated_data.get("exam_45_no_2", instance.exam_45_no_2)
        instance.exam_finally = validated_data.get("exam_finally", instance.exam_finally)
        instance.avg_point = validated_data.get("avg_point", instance.avg_point)
        instance.save()
        return instance

class ListPerformanceSerializer(serializers.ModelSerializer):
    school_year = serializers.SerializerMethodField()
    classes = serializers.SerializerMethodField()
    student = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Performance
        fields = [
            'school_year',
            'classes',
            'student',
            'teacher',
            'medium_score_section_1',
            'medium_score_section_2',
            'medium_score_overall',
            'conduct_classification_section_1',
            'conduct_classification_section_2',
            'conduct_classification_overall',
            'positive_section_1',
            'positive_section_2',
            'negative_section_1',
            'negative_section_2',
            'days_off_section_1',
            'days_off_section_2',
            'days_off_overall',
            'rank_section_1',
            'rank_section_2',
            'rank_overall',
            'note_overall',
            'created_at',
            'updated_at'
        ]

    def get_student(self, obj):
        if not obj.student:
            return None
        return {
            'id': getattr(obj.student, 'id'), 
            'full_name': getattr(obj.student, 'full_name'),
            'gender': getattr(obj.student, 'gender'),
            'birthday': getattr(obj.student, 'birthday'),
            'address': getattr(obj.student, 'address'),
            'nation': getattr(obj.student, 'nation'),
            'religion': getattr(obj.student, 'religion'),
            'father_name': getattr(obj.student, 'father_name'),
            'father_job': getattr(obj.student, 'father_job'),
            'mother_name': getattr(obj.student, 'mother_name'),
            'mother_job': getattr(obj.student, 'mother_job'),
        }

    def get_school_year(self, obj):
        if not obj.school_year:
            return None
        return {'id': getattr(obj.school_year, 'id'), 'name': getattr(obj.school_year, 'name')}

    def get_classes(self, obj):
        if not obj.classes:
            return None
        return {'id': getattr(obj.classes, 'id'), 'name': getattr(obj.classes, 'name')}

    def get_teacher(self, obj):
        if not obj.teacher:
            return None
        return {
            'id': getattr(obj.teacher, 'id'),
            'full_name': getattr(obj.teacher, 'full_name'),
            'phone': getattr(obj.teacher, 'phone'),
            'email': getattr(obj.teacher, 'email'),
            'address': getattr(obj.teacher, 'address'),
            'specialize': getattr(obj.teacher, 'specialize'),
            'position': getattr(obj.teacher, 'position'),
        }

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_updated_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

class PerformanceCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Performance
        fields = [
            'school_year',
            'classes',
            'student',
            'teacher',
            'medium_score_section_1',
            'medium_score_section_2',
            'medium_score_overall',
            'conduct_classification_section_1',
            'conduct_classification_section_2',
            'conduct_classification_overall',
            'positive_section_1',
            'positive_section_2',
            'negative_section_1',
            'negative_section_2',
            'days_off_section_1',
            'days_off_section_2',
            'days_off_overall',
            'rank_section_1',
            'rank_section_2',
            'rank_overall',
            'note_overall',
        ]

    def create(self, validated_data):
        performance = Performance.objects.create(**validated_data)
        return performance

class PerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Performance
        fields = [
            'school_year',
            'classes',
            'student',
            'teacher',
            'medium_score_section_1',
            'medium_score_section_2',
            'medium_score_overall',
            'conduct_classification_section_1',
            'conduct_classification_section_2',
            'conduct_classification_overall',
            'positive_section_1',
            'positive_section_2',
            'negative_section_1',
            'negative_section_2',
            'days_off_section_1',
            'days_off_section_2',
            'days_off_overall',
            'rank_section_1',
            'rank_section_2',
            'rank_overall',
            'note_overall',
            'created_at',
            'updated_at'
        ]
    
    def update(self, instance, validated_data):
        instance.school_year = validated_data.get("school_year", instance.school_year)
        instance.student = validated_data.get("student", instance.student)
        instance.classes = validated_data.get("classes", instance.classes)
        instance.teacher = validated_data.get("teacher", instance.teacher)
        instance.medium_score_section_1 = validated_data.get("medium_score_section_1", instance.medium_score_section_1)
        instance.medium_score_section_2 = validated_data.get("medium_score_section_2", instance.medium_score_section_2)
        instance.medium_score_overall = validated_data.get("medium_score_overall", instance.medium_score_overall)
        instance.conduct_classification_section_1 = validated_data.get("conduct_classification_section_1", instance.conduct_classification_section_1)
        instance.conduct_classification_section_2 = validated_data.get("conduct_classification_section_2", instance.conduct_classification_section_2)
        instance.conduct_classification_overall = validated_data.get("conduct_classification_overall", instance.conduct_classification_overall)
        instance.positive_section_1 = validated_data.get("positive_section_1", instance.positive_section_1)
        instance.positive_section_2 = validated_data.get("positive_section_2", instance.positive_section_2)
        instance.negative_section_1 = validated_data.get("negative_section_1", instance.negative_section_1)
        instance.negative_section_2 = validated_data.get("negative_section_2", instance.negative_section_2)
        instance.days_off_section_1 = validated_data.get("days_off_section_1", instance.days_off_section_1)
        instance.days_off_section_2 = validated_data.get("days_off_section_2", instance.days_off_section_2)
        instance.days_off_overall = validated_data.get("days_off_overall", instance.days_off_overall)
        instance.rank_section_1 = validated_data.get("rank_section_1", instance.rank_section_1)
        instance.rank_section_2 = validated_data.get("rank_section_2", instance.rank_section_2)
        instance.rank_overall = validated_data.get("rank_overall", instance.rank_overall)
        instance.note_overall = validated_data.get("note_overall", instance.note_overall)
        instance.save()
        return instance



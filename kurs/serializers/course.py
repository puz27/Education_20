from rest_framework import serializers
from kurs.models import Course, Lesson
from kurs.serializers.lesson import LessonSerializer
from kurs.validators import validator_scan_links


class CourseSerializer(serializers.ModelSerializer):
    description = serializers.CharField(validators=[validator_scan_links])

    class Meta:
        model = Course
        fields = "__all__"


class CourseListLessonSerializer(serializers.ModelSerializer):
    # get all lessons for course
    lesson = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = ("title", "lesson")


class CourseCountSerializer(serializers.ModelSerializer):
    # get count of lessons for course
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, obj):
        return obj.lesson.count()

    class Meta:
        model = Course
        fields = "__all__"

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from kurs.models import Course, Lesson
from kurs.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):

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

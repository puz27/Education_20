from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from kurs.models import Course, Lesson


class CourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class CourceListSerializer(serializers.ModelSerializer):
    # get lesson from table use field "title"
    lesson = SlugRelatedField(slug_field="title", queryset=Lesson.objects.all())
    lessons_count = SerializerMethodField()

    def get_lessons_count(self, cource):
        return Course.objects.filter(lesson=cource.lesson).count()

    class Meta:
        model = Course
        fields = ("title", "lesson", "lessons_count")


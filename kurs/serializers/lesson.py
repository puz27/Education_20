from rest_framework import serializers
from kurs.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        filter = "__all__"

from rest_framework import serializers
from kurs.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Lesson
        fields = "__all__"



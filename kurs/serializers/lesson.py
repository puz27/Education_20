from rest_framework import serializers
from kurs.models import Lesson
from kurs.validators import validator_scan_links


class LessonSerializer(serializers.ModelSerializer):
    description = serializers.CharField(validators=[validator_scan_links])

    class Meta:
        model = Lesson
        fields = "__all__"




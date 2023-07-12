from rest_framework import serializers
from kurs.models import Course


class CourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        filter = "__all__"


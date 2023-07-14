from rest_framework import viewsets
from kurs.models import Course
from kurs.serializers.course import CourceSerializer, CourceListSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourceListSerializer


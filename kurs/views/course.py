from rest_framework import viewsets
from kurs.models import Course
from kurs.serializers.course import CourseSerializer, CourseListLessonSerializer, CourseCountSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseCountSerializer

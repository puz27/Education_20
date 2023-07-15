from rest_framework import viewsets
from kurs.serializers.lesson import LessonSerializer
from kurs.models import Lesson
from kurs.models import Course
from kurs.serializers.course import CourseSerializer, CourseListLessonSerializer, CourseCountSerializer
from rest_framework import generics


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseListLessonView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListLessonSerializer


class CourseCountView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCountSerializer


# class CourseViewSet(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseCountSerializer
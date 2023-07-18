from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from kurs.serializers.lesson import LessonSerializer
from kurs.models import Lesson
from kurs.models import Course
from kurs.serializers.course import CourseSerializer, CourseListLessonSerializer, CourseCountSerializer
from rest_framework import generics
from kurs.permissions import IsStaff, IsOwner


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsStaff | IsOwner]


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class CourseListLessonView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListLessonSerializer
    permission_classes = [IsAuthenticated]


class CourseCountView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCountSerializer
    permission_classes = [IsAuthenticated]


# class CourseViewSet(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseCountSerializer
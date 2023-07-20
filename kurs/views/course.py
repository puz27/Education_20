from kurs.models import Course
from kurs.pagination import DataPaginator
from kurs.serializers.course import CourseSerializer, CourseListLessonSerializer, CourseCountSerializer
from rest_framework import generics
from kurs.permissions import IsStaff, IsOwner


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsOwner | IsStaff]
    pagination_class = DataPaginator


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsStaff | IsOwner]


class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsStaff | IsOwner]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsStaff | IsOwner]


class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsStaff | IsOwner]


class CourseListLessonView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListLessonSerializer
    permission_classes = [IsStaff | IsOwner]


class CourseCountView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCountSerializer
    permission_classes = [IsStaff | IsOwner]


# class CourseViewSet(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseCountSerializer
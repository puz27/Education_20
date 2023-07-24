from rest_framework import generics
from kurs.pagination import DataPaginator
from kurs.permissions import IsOwner, IsStaff
from kurs.serializers.lesson import LessonSerializer
from kurs.models import Lesson


class LessonListView(generics.ListAPIView):
    """ All lessons """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsStaff | IsOwner]
    pagination_class = DataPaginator


class LessonDetailView(generics.RetrieveAPIView):
    """ Detailed information about lesson """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsStaff | IsOwner]


class LessonCreateView(generics.CreateAPIView):
    """ Create lesson with owner information"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsStaff | IsOwner]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonUpdateView(generics.UpdateAPIView):
    """ Update information in lesson """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsStaff | IsOwner]


class LessonDeleteView(generics.DestroyAPIView):
    """ Delete lesson """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsStaff | IsOwner]

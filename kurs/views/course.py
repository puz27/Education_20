from rest_framework.viewsets import ModelViewSet
from kurs.models import Course
from kurs.serializers.course import CourceSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourceSerializer

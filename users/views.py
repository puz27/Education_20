from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from kurs.serializers.lesson import LessonSerializer
from users.models import Users
from users.serializers.users import UserSerializer


class UsersListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UsersDetailView(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = LessonSerializer


class UsersCreateView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = LessonSerializer


class UsersUpdateView(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = LessonSerializer


class UsersDeleteView(generics.DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = LessonSerializer

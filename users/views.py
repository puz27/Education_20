from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from kurs.serializers.lesson import LessonSerializer
from users.models import Users
from users.serializers.users import UserSerializer


# class IsAdminOrReadOnly(BasePermission):
#
#     def has_permission(self, request, view):
#
#         if request.method in SAFE_METHODS:
#             return True
#         return request.user.is_authenticated


class UsersListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UsersDetailView(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UsersCreateView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UsersUpdateView(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UsersDeleteView(generics.DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

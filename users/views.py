from rest_framework.viewsets import ModelViewSet
from users.models import Users
from users.serializers.users import UserSerializer


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

from rest_framework import generics
from kurs.pagination import DataPaginator
from kurs.permissions import IsOwner, IsStaff
from kurs.serializers.subscription import SubscriptionSerializer
from kurs.models import Subscription


class SubscriptionListView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsStaff | IsOwner]
    pagination_class = DataPaginator


class SubscriptionCreateView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsStaff | IsOwner]

    def perform_create(self, serializer):
        new_subscription = serializer.save()
        new_subscription.owner = self.request.user
        new_subscription.save()


class SubscriptionDeleteView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsStaff | IsOwner]


from rest_framework import generics
from kurs.pagination import DataPaginator
from kurs.permissions import IsOwner, IsStaff
from kurs.serializers.subscription import SubscriptionSerializer
from kurs.models import Subscription
from kurs.servises import sendmail


class SubscriptionListView(generics.ListAPIView):
    """ All subscriptions """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsStaff | IsOwner]
    pagination_class = DataPaginator


class SubscriptionCreateView(generics.CreateAPIView):
    """ Create subscription with owner information"""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsStaff | IsOwner]

    def perform_create(self, serializer):
        new_subscription = serializer.save()
        new_subscription.owner = self.request.user
        new_subscription.save()


class SubscriptionUpdateView(generics.UpdateAPIView):
    """ Update information in subscription """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsStaff | IsOwner]

    def put(self, request, *args, **kwargs):
        sendmail("test@test.ru")
        return self.update(request, *args, **kwargs)


class SubscriptionDeleteView(generics.DestroyAPIView):
    """ Delete subscription """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsStaff | IsOwner]


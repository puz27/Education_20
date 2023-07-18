from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from kurs.serializers.payment import PaymentSerializer
from kurs.models import Payment
from rest_framework.filters import OrderingFilter
from kurs.permissions import IsOwner, IsStaff


class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff | IsOwner]


class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff | IsOwner]


class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff | IsOwner]

    def perform_create(self, serializer):
        new_payment = serializer.save()
        new_payment.owner = self.request.user
        new_payment.save()


class PaymentUpdateView(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff | IsOwner]


class PaymentDeleteView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff | IsOwner]


class PaymentFilter(generics.ListAPIView):
    permission_classes = [IsStaff | IsOwner]
    # filters
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment')
    ordering_fields = ('date',)




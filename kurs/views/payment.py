from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from kurs.serializers.payment import PaymentSerializer
from kurs.models import Payment
from rest_framework.filters import OrderingFilter


class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentUpdateView(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDeleteView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentFilter(generics.ListAPIView):
    # filters
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment')
    ordering_fields = ('date',)



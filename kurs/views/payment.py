from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from kurs.pagination import DataPaginator
from kurs.serializers.payment import PaymentSerializer
from kurs.models import Payment
from rest_framework.filters import OrderingFilter
from kurs.permissions import IsOwner, IsStaff
from kurs.servises import Customer, PaymentCustomer
from rest_framework import serializers

class PaymentListView(generics.ListAPIView):
    """ All payments """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff | IsOwner]
    pagination_class = DataPaginator


class PaymentDetailView(generics.RetrieveAPIView):
    """ Detailed information about payment """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff | IsOwner]


class PaymentCreateView(generics.CreateAPIView):
    """ Create payment with owner information and cost of course"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff | IsOwner]

    def perform_create(self, serializer):
        new_payment = serializer.save()
        new_payment.owner = self.request.user
        new_payment.save()
        # get user
        new_customer = Customer(self.request.user)
        new_customer.create_customer()
        customer_id = new_customer.retrieve_customer()["id"]
        # get user_id / cost of course and make request
        new_payment = PaymentCustomer(customer_id, new_payment.course.cost)
        new_payment.create_payment()


class PaymentRemoteDetailView(generics.RetrieveAPIView):
    """ Detailed information about payment from remote base"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff | IsOwner]


class PaymentUpdateView(generics.UpdateAPIView):
    """ Update information in payment """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff | IsOwner]


class PaymentDeleteView(generics.DestroyAPIView):
    """ Delete payment """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsStaff | IsOwner]


class PaymentFilter(generics.ListAPIView):
    """ Payment and use filters """
    permission_classes = [IsStaff | IsOwner]
    # filters
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment')
    ordering_fields = ('date',)




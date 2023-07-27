from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from kurs.pagination import DataPaginator
from kurs.serializers.payment import PaymentSerializer, PaymentRemoteSerializer
from kurs.models import Payment
from rest_framework.filters import OrderingFilter
from kurs.permissions import IsOwner, IsStaff
import stripe

stripe.api_key = "sk_test_51NXPaKCn4C5dva66mINywzPgyNFznygCyoFq01lCmrEHwkmEGzEFLfp36l1Nzx1Gt9jJxCOcrfbKY9R3HCxSfkjQ00NkNSsW8K"

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
        # create user
        new_customer = self.request.user

        request_user = stripe.Customer.create(
            name=new_customer.email,
            email=new_customer.email,
        )
        current_id = request_user.id
        print(current_id)
        # create transaction

        request_payment = stripe.PaymentIntent.create(
            amount=new_payment.course.cost,
            currency="usd",
            automatic_payment_methods={"enabled": True},
            customer=current_id,
        )
        print(request_payment.id)

        new_payment = serializer.save()
        new_payment.remote_id = request_payment.id
        new_payment.save()


class PaymentRemoteDetailView(generics.RetrieveAPIView):
    """ Detailed information about payment from remote base"""
    queryset = Payment.objects.all()
    serializer_class = PaymentRemoteSerializer
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




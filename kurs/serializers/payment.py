from rest_framework import serializers
from kurs.models import Payment, Course
from kurs.servises import PaymentCustomer
import stripe


class PaymentSerializer(serializers.ModelSerializer):
    # remote_info = serializers.SerializerMethodField()

    def create(self, validated_data):
        new_payment = Payment.objects.create(**validated_data)
        return new_payment

    class Meta:
        model = Payment
        fields = "__all__"


class PaymentRemoteSerializer(serializers.ModelSerializer):
    remote_info = serializers.SerializerMethodField()

    def get_remote_info(self, obj):
        remote_id = obj.remote_id
        stripe.PaymentIntent.retrieve(remote_id)
        print(stripe.PaymentIntent.retrieve(remote_id)["amount"])
        return stripe.PaymentIntent.retrieve(remote_id)["amount"]

    class Meta:
        model = Payment
        fields = "__all__"


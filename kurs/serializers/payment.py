from rest_framework import serializers
from kurs.models import Payment, Course
from kurs.servises import PaymentCustomer


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

    class Meta:
        model = Payment
        fields = "__all__"

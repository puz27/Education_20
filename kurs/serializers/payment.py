from rest_framework import serializers
from kurs.models import Payment, Course


class PaymentSerializer(serializers.ModelSerializer):
    # remote_info = serializers.SerializerMethodField()

    def create(self, validated_data):
        new_payment = Payment.objects.create(**validated_data)
        return new_payment

    class Meta:
        model = Payment
        fields = "__all__"


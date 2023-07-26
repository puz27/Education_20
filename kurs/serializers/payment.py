from rest_framework import serializers
from kurs.models import Payment, Course
from kurs.servises import convert_price, PaymentCustomer


class PaymentSerializer(serializers.ModelSerializer):
    # course_amount = serializers.SerializerMethodField()

    def create(self, validated_data):
        new_payment = Payment.objects.create(**validated_data)
        return new_payment

    # def get_course_amount(self, obj):
    #     """ """
    #     print(obj.course)
    #     return obj.course

    class Meta:
        model = Payment
        fields = "__all__"


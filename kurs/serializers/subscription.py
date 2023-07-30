from rest_framework import serializers
from kurs.models import Subscription
from kurs.tasks import send_information


class SubscriptionSerializer(serializers.ModelSerializer):

    def save(self, instance, validated_data):
        send_information.delay()

    class Meta:
        model = Subscription
        fields = "__all__"

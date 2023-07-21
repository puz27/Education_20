from rest_framework import serializers
from kurs.models import Course, Subscription
from kurs.serializers.lesson import LessonSerializer
from kurs.serializers.subscription import SubscriptionSerializer
from kurs.validators import validator_scan_links


class CourseSerializer(serializers.ModelSerializer):
    description = serializers.CharField(validators=[validator_scan_links])
    subscribed_subscriptions = serializers.SerializerMethodField()
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_subscribed_subscriptions(self, obj):
        """ Show subscription of owners """
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Subscription.objects.filter(owner=request.user, course=obj).exists()
        return False

    def get_lessons_count(self, obj):
        """ Show counts of lessons in course """
        return obj.lesson.count()

    class Meta:
        model = Course
        fields = "__all__"


class CourseListLessonSerializer(serializers.ModelSerializer):
    # get all lessons for course
    lesson = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = ("title", "lesson")


class CourseCountSerializer(serializers.ModelSerializer):
    # get count of lessons for course/ add this functional to CourseSerializer
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, obj):
        return obj.lesson.count()

    class Meta:
        model = Course
        fields = "__all__"

from django.db import models
from config import settings


class Course(models.Model):

    title = models.CharField(max_length=100, verbose_name="course_name")
    description = models.TextField(null=True, blank=True, verbose_name="course_description")
    image = models.ImageField(upload_to="images", null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"


class Lesson(models.Model):

    title = models.CharField(max_length=100, verbose_name="lesson_name")
    description = models.TextField(null=True, blank=True, verbose_name="lesson_description")
    image = models.ImageField(upload_to="images", null=True, blank=True)
    course = models.ForeignKey("Course", on_delete=models.SET_NULL, null=True, blank=True, related_name="lesson")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "lesson"
        verbose_name_plural = "lessons"


class Payment(models.Model):

    user = models.CharField(max_length=100, verbose_name="user_name")
    date = models.DateField()
    lesson = models.ForeignKey("Lesson", on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey("Course", on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.IntegerField(null=False, blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)


class Subscription(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey("Course", on_delete=models.CASCADE, verbose_name='course', related_name="subscription")
    is_subscribed = models.BooleanField(default=False, verbose_name='user_subscription_on_course')

    def __str__(self):
        return self.owner

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

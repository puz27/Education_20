from django.db import models


class Course(models.Model):

    title = models.CharField(max_length=100, verbose_name="product_name")
    description = models.TextField(null=True, blank=True, verbose_name="product_description")
    image = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"


class Lesson(models.Model):

    title = models.CharField(max_length=100, verbose_name="product_name")
    description = models.TextField(null=True, blank=True, verbose_name="product_description")
    image = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "lesson"
        verbose_name_plural = "lessons"

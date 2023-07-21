from django.urls import path
from rest_framework.routers import DefaultRouter
from kurs.views.lesson import LessonDetailView, LessonListView, LessonCreateView, LessonDeleteView, LessonUpdateView
from kurs.views.payment import PaymentDetailView, PaymentListView, PaymentCreateView, PaymentDeleteView, \
    PaymentUpdateView, PaymentFilter
from kurs.views.course import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, CourseCountView, CourseListLessonView
from kurs.views.subscription import SubscriptionListView, SubscriptionCreateView, SubscriptionDeleteView

app_name = "kurs"


urlpatterns = [
    # lessons
    path("lesson/", LessonListView.as_view(), name="show_all_lessons"),
    path("lesson/<int:pk>/", LessonDetailView.as_view(), name="lesson_show"),
    path("lesson/create/", LessonCreateView.as_view(), name="lesson_create"),
    path("lesson/update/<int:pk>/", LessonUpdateView.as_view(), name="lesson_update"),
    path("lesson/delete/<int:pk>/", LessonDeleteView.as_view(), name="lesson_delete"),
    # payment
    path("payment/", PaymentListView.as_view(), name="show_all_payments"),
    path("payment/<int:pk>/", PaymentDetailView.as_view(), name="lesson_show"),
    path("payment/create/", PaymentCreateView.as_view(), name="lesson_create"),
    path("payment/update/<int:pk>/", PaymentUpdateView.as_view(), name="lesson_update"),
    path("payment/delete/<int:pk>/", PaymentDeleteView.as_view(), name="lesson_delete"),
    path("payment/filter/", PaymentFilter.as_view()),
    # course
    path("course/", CourseListView.as_view(), name="show_all_courses"),
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course_show"),
    path("course/create/", CourseCreateView.as_view(), name="course_create"),
    path("course/update/<int:pk>/", CourseUpdateView.as_view(), name="course_update"),
    path("course/delete/<int:pk>/", CourseDeleteView.as_view(), name="course_delete"),
    # subscription
    path("subscription/", SubscriptionListView.as_view(), name="show_all_subscriptions"),
    path("subscription/create/", SubscriptionCreateView.as_view(), name="subscription_create"),
    path("subscription/delete/<int:pk>/", SubscriptionDeleteView.as_view(), name="subscription_delete"),
    # get all lessons for course
    path("course/lesson-list/", CourseListLessonView.as_view()),
    # get counts of lessons for course
    path("course/lesson-count/", CourseCountView.as_view()),
]

# course
# router = DefaultRouter()
# router.register(r"course", CourseViewSet, basename="course")
# urlpatterns += router.urls

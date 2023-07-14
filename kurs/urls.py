from django.urls import path
from rest_framework.routers import DefaultRouter
from kurs.views.lesson import LessonDetailView, LessonListView, LessonCreateView, LessonDeleteView, LessonUpdateView
from kurs.views.payment import PaymentDetailView, PaymentListView, PaymentCreateView, PaymentDeleteView, PaymentUpdateView
from kurs.views.course import CourseViewSet

app_name = "kurs"


urlpatterns = [
    # lessons
    path("lesson/", LessonListView.as_view()),
    path("lesson/<int:pk>/", LessonDetailView.as_view(), name="lesson_show"),
    path("lesson/create/", LessonCreateView.as_view(), name="lesson_create"),
    path("lesson/update/<int:pk>/", LessonUpdateView.as_view(), name="lesson_update"),
    path("lesson/delete/<int:pk>/", LessonDeleteView.as_view(), name="lesson_delete"),
    # payment
    path("payment/", PaymentListView.as_view()),
    path("payment/<int:pk>/", PaymentDetailView.as_view(), name="lesson_show"),
    path("payment/create/", PaymentCreateView.as_view(), name="lesson_create"),
    path("payment/update/<int:pk>/", PaymentUpdateView.as_view(), name="lesson_update"),
    path("payment/delete/<int:pk>/", PaymentDeleteView.as_view(), name="lesson_delete"),

]
# course
router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")
urlpatterns += router.urls

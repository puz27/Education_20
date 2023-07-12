from django.urls import path
from rest_framework.routers import DefaultRouter
from kurs.views.lesson import LessonDetailView, LessonListView, LessonCreateView, LessonDeleteView, LessonUpdateView
from kurs.views.course import CourseViewSet

app_name = "kurs"


urlpatterns = [
    path("lesson/", LessonListView.as_view()),
    path("lesson/<int:pk>/", LessonDetailView.as_view(), name="lesson_show"),
    path("lesson/create/", LessonCreateView.as_view(), name="lesson_create"),
    path("lesson/update/<int:pk>/", LessonUpdateView.as_view(), name="lesson_update"),
    path("lesson/delete/<int:pk>/", LessonDeleteView.as_view(), name="lesson_delete"),

]

router = DefaultRouter()
router.register(r"course", CourseViewSet)
urlpatterns += router.urls

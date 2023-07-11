from django.urls import path
from kurs.views.course import CourseViewSet
from kurs.views.lesson import LessonDetailView, LessonListView, LessonCreateView, LessonDeleteView, LessonUpdateView

app_name = "cource"

urlpatterns = [
    path("", LessonListView.as_view()),
    path("<int:pk>", LessonDetailView.as_view()),
    path("<int:pk>/create", LessonCreateView.as_view()),
    path("<int:pk>/update", LessonUpdateView.as_view()),
    path("<int:pk>/delete", LessonDeleteView.as_view()),
]

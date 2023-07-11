from django.urls import path
from kurs.views.course import CourseViewSet
from kurs.views.lesson import LessonDetailView, LessonListView, LessonCreateView, LessonDeleteView, LessonUpdateView

app = "kurs"

urlpatterns = [
    path("lesson/", LessonListView.as_view()),
    path("lesson/<int:pk>", LessonDetailView.as_view()),
    path("lesson/<int:pk>", LessonCreateView.as_view()),
    path("lesson/<int:pk>/update", LessonUpdateView.as_view()),
    path("lesson/<int:pk>/delete", LessonDeleteView.as_view()),
]

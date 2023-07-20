from rest_framework.test import APITestCase
from kurs.models import Lesson, Course
from django.urls import reverse
from rest_framework import status
from users.models import Users


class LessonTestCase(APITestCase):

    def setUp(self):
        """ Prepare testing """
        self.user = Users(
            email="test3@gmail.com"
        )
        self.user.set_password("test3")
        self.user.save()

        response = self.client.post(
            # reverse("users:take_token"),
            "/api/v1/users/token/",
            {"email": "test3@gmail.com", "password": "test3"}
        )

        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        self.course = Course.objects.create(
            title="Test Course",
            description="Test Course description",
        )

        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            description="Test Lesson description",
            course=self.course
        )

    def test_get_lessons(self):
        response = self.client.get("/api/v1/lesson/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_lesson(self):
        data = {"title": "Test Lesson23",
                "description": "123333"
                }

        response = self.client.post("/api/v1/lesson/create/", data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_validate_lesson(self):
        data = {"title": "Test Lesson23",
                "description": "https://vk.com"
                }

        response = self.client.post("/api/v1/lesson/create/", data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_update_lesson(self):
        data = {"title": "NEW", "description": "NEW"}

        data_answer = {
            "title": "NEW",
            "description": "NEW"
        }
        response = self.client.post("/api/v1/lesson/update/", data)
        self.assertEqual(response.json(), data_answer)



    # def test_get_courses(self):
    #
    #     response = self.client.get(
    #         reverse("kurs:show_all_courses")
    #     )
    #
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
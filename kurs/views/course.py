from kurs.models import Course
from kurs.pagination import DataPaginator
from kurs.serializers.course import CourseSerializer, CourseListLessonSerializer, CourseCountSerializer
from rest_framework import generics
from kurs.permissions import IsStaff, IsOwner
from kurs.servises import Customer, PaymentCustomer


class CourseListView(generics.ListAPIView):
    """ All courses """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsOwner | IsStaff]
    pagination_class = DataPaginator


class CourseDetailView(generics.RetrieveAPIView):
    """ Detailed information about course """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsStaff | IsOwner]


class CourseCreateView(generics.CreateAPIView):
    """ Create course with owner information"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsStaff | IsOwner]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

        new_customer = Customer(self.request.user)
        new_customer.create_customer()
        customer_id = new_customer.retrieve_customer()["id"]
        print(serializer["cost"])

        new_payment = PaymentCustomer(customer_id, 123)
        new_payment.create_payment()


class CourseUpdateView(generics.UpdateAPIView):
    """ Update information in course """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsStaff | IsOwner]


class CourseDeleteView(generics.DestroyAPIView):
    """ Delete course """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsStaff | IsOwner]


class CourseListLessonView(generics.ListAPIView):
    """ All lessons in course"""
    queryset = Course.objects.all()
    serializer_class = CourseListLessonSerializer
    permission_classes = [IsStaff | IsOwner]


class CourseCountView(generics.ListAPIView):
    """ Count of lessons """
    queryset = Course.objects.all()
    serializer_class = CourseCountSerializer
    permission_classes = [IsStaff | IsOwner]

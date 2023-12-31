from django.core.management import BaseCommand
from users.models import Users


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = Users.objects.create(
            email="admin@gmail.com",
            first_name="admin",
            last_name="admin",
            is_superuser=True,
            is_staff=True,
            is_active=True
            )

        user.set_password("admin")
        user.save()

        user = Users.objects.create(
            email="test@gmail.com",
            first_name="test",
            last_name="test",
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user.set_password("test")
        user.save()

        user = Users.objects.create(
            email="test2@gmail.com",
            first_name="test2",
            last_name="test2",
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user.set_password("test2")
        user.save()

        user = Users.objects.create(
            email="test3@gmail.com",
            first_name="test3",
            last_name="test3",
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user.set_password("test3")
        user.save()

        user = Users.objects.create(
            email="moderator@gmail.com",
            first_name="moderator",
            last_name="moderator",
            is_superuser=False,
            is_staff=True,
            is_active=True
        )

        user.set_password("moderator")
        user.save()

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

        user.set_password("123456")
        user.save()

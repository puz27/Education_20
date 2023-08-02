import json
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings
from django_celery_beat.models import PeriodicTask, \
    IntervalSchedule


# celery -A config worker -l INFO
# celery -A config beat -l info -S django

# def set_schedule(*args, **kwargs):
#     schedule, created = IntervalSchedule.objects.get_or_create(
#          every=30,
#          period=IntervalSchedule.SECONDS,
#      )
#
#     PeriodicTask.objects.create(
#          interval=schedule,
#          name='block_inactive_users',
#          task='users.tasks.block_inactive_users',
#          args=json.dumps(['arg1', 'arg2']),
#          kwargs=json.dumps({
#             'be_careful': True,
#          }),
#          expires=datetime.utcnow() + timedelta(seconds=30)
#      )

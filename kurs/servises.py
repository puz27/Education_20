import json
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings
from django_celery_beat.models import PeriodicTask, \
    IntervalSchedule

# Создаем интервал для повтора
# schedule, created = IntervalSchedule.objects.get_or_create(
#      every=30,
#      period=IntervalSchedule.SECONDS,
#  )

# Создаем задачу для повторения
# PeriodicTask.objects.create(
#      interval=schedule,
#      name='Importing contacts',
#      task='kurs.tasks.send_information',
#      args=json.dumps(['arg1', 'arg2']),
#      kwargs=json.dumps({
#         'be_careful': True,
#      }),
#      expires=datetime.utcnow() + timedelta(seconds=30)
#  )


def sendmail(to):
    send_mail(f"Your subscription on site.",
              f"Update information about your subscription.",
              settings.EMAIL_HOST_USER,
              [to],
              fail_silently=False)

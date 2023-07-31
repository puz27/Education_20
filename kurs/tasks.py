from celery import shared_task
from users.models import Users
from datetime import datetime, timedelta


# @shared_task
def block_inactive_users():
    need_date = (datetime.today() - timedelta(30)).date()
    get_users = Users.objects.all()
    print(need_date)
    for user in get_users:
        if user.last_login:
            last = user.last_login.date()
            print(last)
            if last > need_date:
                print(f"Block user{user.last_login}.")
                user.is_active = False
                user.save()





from celery import shared_task
from users.models import Users


# @shared_task
def block_inactive_users():
    print("Block inactive users.")
    get_users = Users.objects.all()
    print(get_users)
    for user in get_users:
        print(user.email_user())
        print(user.last_login)



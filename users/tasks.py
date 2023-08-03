from django.utils.timezone import now
from celery import shared_task
from users.models import Users


class SetLastVisitMiddleware(object):
    def process_response(self, request, response):
        if request.user.is_authenticated():
            # Update last visit time after request finished processing.
            Users.objects.filter(pk=request.user.pk).update(last_login=now())
        return response


@shared_task(name="block_inactive_users")
def block_inactive_users():
    print("Block users !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")
    # need_date = (datetime.today() - timedelta(30)).date()
    # get_users = Users.objects.all()
    # print(need_date)
    # for user in get_users:
    #     if user.last_login:
    #         last = user.last_login.date()
    #         print(last)
    #         if last < need_date:
    #             print(f"Block user{user.last_login}.")
    #             user.is_active = False
    #             user.save()

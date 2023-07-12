from rest_framework.routers import DefaultRouter
from users.views import UsersViewSet

app_name = "users"


urlpatterns = [
]

router = DefaultRouter()
router.register(r"users", UsersViewSet, basename="users")
urlpatterns += router.urls

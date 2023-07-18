from rest_framework.routers import DefaultRouter
from users.views import UsersListView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = "users"


urlpatterns = [
    path("show/", UsersListView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

]

# router = DefaultRouter()
# router.register(r"users", UsersViewSet, basename="users")
# urlpatterns += router.urls

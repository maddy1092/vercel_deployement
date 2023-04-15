from django.urls import path

from users.apis.v1.views import (
    UserCreateAPIView,
)

app_name = "users"

urlpatterns = [
    path("register", UserCreateAPIView.as_view(), name="register")
]
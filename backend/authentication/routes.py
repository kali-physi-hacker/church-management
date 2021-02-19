from django.urls import path

from .views import LoginApiView

urlpatterns = [
    path("user/login/", LoginApiView.as_view({"post": "login"}), name="login")
]

app_name = "authentication"

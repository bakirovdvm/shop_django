from django.urls import path
from .views import SignInView


app_name = "api"

urlpatterns = [
    path("sign-in", SignInView.as_view(), name="login"),
]
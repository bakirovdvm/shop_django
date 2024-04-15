from django.urls import path
from .views import ProfileView, PasswordView


app_name = "my_profile"

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/password", PasswordView.as_view(), name="changePassword"),
]
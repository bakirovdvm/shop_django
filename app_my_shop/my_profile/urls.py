from django.urls import path
from .views import ProfileView, PasswordView, AvatarView


app_name = "my_profile"

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/password", PasswordView.as_view(), name="changePassword"),
    path("profile/avatar", AvatarView.as_view(), name="changeAvatar"),
]
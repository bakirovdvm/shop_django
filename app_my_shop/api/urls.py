from django.urls import path
from .views import SignInView, signOut, SignUpView


app_name = "api"

urlpatterns = [
    path("sign-in", SignInView.as_view(), name="login"),
    path("sign-up", SignUpView.as_view(), name="logup"),
    path('sign-out', signOut)
]
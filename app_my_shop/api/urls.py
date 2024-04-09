from django.urls import path
from .views import SignInView, signOut


app_name = "api"

urlpatterns = [
    path("sign-in", SignInView.as_view(), name="login"),
    path('sign-out', signOut)
]
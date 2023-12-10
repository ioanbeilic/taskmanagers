from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("sign-up", views.signup, name="sign_up"),
    path("sign-in", views.signin, name="sign_in"),
]

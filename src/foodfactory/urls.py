from django.urls import path

from . import views

app_name = "foodfactory"

urlpatterns = [path("", views.home, name="home")]

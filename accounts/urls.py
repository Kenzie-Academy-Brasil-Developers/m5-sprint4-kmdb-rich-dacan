from django.urls import path

from . import views

urlpatterns = [
    path("users/login/", views.LoginView.as_view()),
]

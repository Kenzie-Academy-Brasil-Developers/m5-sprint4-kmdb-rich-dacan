from django.urls import path

from . import views

urlpatterns = [
    path("users/login/", views.CredentialsView.as_view()),
    path("users/register/", views.RegisterView.as_view()),
]

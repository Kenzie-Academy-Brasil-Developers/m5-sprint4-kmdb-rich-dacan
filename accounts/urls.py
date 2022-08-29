from django.urls import path

from . import views

urlpatterns = [
    path("users/", views.RetrieveAccountsView.as_view()),
    path("users/<int:account_id>/", views.RetrieveAccountView.as_view()),
    path("users/login/", views.LoginView.as_view()),
    path("users/register/", views.RegisterView.as_view()),
]

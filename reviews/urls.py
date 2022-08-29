from django.urls import path

from . import views

urlpatterns = [
    path("movies/<movie_id>/reviews/<review_id>/", views.ReviewDetailView.as_view()),
    path("movies/<movie_id>/reviews/", views.ReviewView.as_view()),
]

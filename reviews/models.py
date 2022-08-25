from django.db import models


class RecommendationChoices(models.TextChoices):
    MUST_WATCH = "Must Watch"
    SHOULD_WATCH = "Should Watch"
    AVOID_WATCH = "Avoid Watch"
    DEFAULT = "No Opinion"


class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField()
    recommendation = models.CharField(
        max_length=50,
        choices=RecommendationChoices.choices,
        default=RecommendationChoices.DEFAULT,
    )
    movie_id = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews"
    )
    critic_id = models.ForeignKey(
        "accounts.Accounts", on_delete=models.CASCADE, related_name="reviews"
    )

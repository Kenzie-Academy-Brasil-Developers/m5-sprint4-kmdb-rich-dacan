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

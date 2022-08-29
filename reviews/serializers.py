from accounts.models import Accounts
from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Review


class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ["id", "first_name", "last_name"]


class ReviewSerializer(serializers.ModelSerializer):

    critic_id = CriticSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "recommendation",
            "movie_id",
            "critic_id",
        ]
        read_only_fields = ["movie_id"]
        extra_kwargs = {"stars": {"min_value": 1, "max_value": 10}}

    def create(self, validated_data):

        account = validated_data.pop("critic")
        movie = validated_data.pop("movie_id")

        is_duplicated = Review.objects.filter(movie_id=movie.id, critic_id=account)

        if is_duplicated:
            raise ValidationError({"detail": "Review already exists."})

        review = Review.objects.create(
            **validated_data, critic_id=account, movie_id=movie
        )

        return review

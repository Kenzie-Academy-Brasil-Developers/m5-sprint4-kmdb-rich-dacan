from genres.models import Genre
from genres.serializer import GenreSerializer
from rest_framework import serializers, status

from movies.models import Movie


class MovieSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField()
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()
    genres = GenreSerializer(many=True)

    def create(self, validated_data: dict):

        genres = validated_data.pop("genres")

        movie_obj = Movie.objects.get_or_create(**validated_data)

        for genre in genres:
            genre, _ = Genre.objects.get_or_create(**genre)
            movie_obj.genres.add(genres)

        return movie_obj

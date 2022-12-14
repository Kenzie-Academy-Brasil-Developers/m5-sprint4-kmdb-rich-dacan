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

        genres_data = [Genre.objects.get_or_create(**genre)[0] for genre in genres]

        movie = Movie.objects.create(**validated_data)
        movie.genres.set(genres_data)

        return movie

    def update(self, genre_db, validated_data):

        for key, value in validated_data.items():

            if key == "genres":
                genres_data = [
                    Genre.objects.get_or_create(**genre)[0] for genre in value
                ]

                genre_db.genres.set(genres_data)
                continue

            setattr(genre_db, key, value)

        genre_db.save()

        return genre_db

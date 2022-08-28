from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Response, status

from .models import Movie
from .permissions import IsAdminOrSafe
from .serializer import MovieSerializer


class MovieView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrSafe]

    def get(self, request):
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid()
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrSafe]

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(movie)

        return Response(serializer.data)

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

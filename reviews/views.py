from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from movies.models import Movie
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Request, Response, status

from .models import Review
from .permissions import IsAdminOrCritic, IsAdminOrOwner
from .serializers import ReviewSerializer


class ReviewView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrCritic]

    def get(self, request: Request, movie_id) -> Response:

        reviews = Review.objects.filter(movie_id=movie_id)
        result_page = self.paginate_queryset(reviews, request, view=self)
        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request, movie_id: int) -> Response:

        movie = get_object_or_404(Movie, id=movie_id)
        serializer = ReviewSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        try:
            serializer.save(movie_id=movie, critic=request.user)

        except ValidationError as err:

            return Response(err.args[0], status.HTTP_403_FORBIDDEN)

        return Response(serializer.data, status.HTTP_201_CREATED)


class ReviewDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrOwner]

    def get(self, request: Request, movie_id, review_id) -> Response:

        review = get_object_or_404(Review, movie_id=movie_id, id=review_id)

        serializer = ReviewSerializer(review)

        return Response(serializer.data)

    def delete(self, request: Request, movie_id, review_id) -> Response:

        review = get_object_or_404(Review, movie_id=movie_id, id=review_id)

        self.check_object_permissions(request, review)

        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

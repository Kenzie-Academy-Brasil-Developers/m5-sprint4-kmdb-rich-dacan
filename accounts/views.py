from django.contrib.auth import authenticate
from rest_framework.views import APIView, Request, Response, status

from accounts.serializer import LoginSerializer, RegisterSerializer


class CredentialsView(APIView):
    def post(self, request: Request) -> Response:

        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        # user = authenticate(
        #     username=serializer.validated_data["username"],
        #     password=serializer.validated_data["password"],
        # )

        user = authenticate(**serializer.validated_data)

        if not user:
            return Response(
                {"detail": "Invalid credentials"}, status.HTTP_404_NOT_FOUND
            )

        return Response({"detail": f"Welcome {user.username}"})


class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

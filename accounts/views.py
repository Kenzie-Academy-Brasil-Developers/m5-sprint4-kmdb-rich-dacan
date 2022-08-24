from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
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

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})

        return Response(
            {"detail": "invalid username or password"}, status.HTTP_400_BAD_REQUEST
        )


class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

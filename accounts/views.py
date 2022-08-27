from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView, Request, Response, status

from accounts.permissions import IsOwnerOrAdmin
from accounts.serializer import AccountSerializer, LoginSerializer

from .models import Accounts


class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request: Request) -> Response:

        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

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


class RetrieveAccountsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:

        accounts = Accounts.objects.all()

        serializer = AccountSerializer(accounts, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class RetrieveAccountView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrAdmin, IsAuthenticated]

    def get(self, request: Request, account_id) -> Response:

        account = get_object_or_404(Accounts, id=account_id)

        self.check_object_permissions(request, account)

        serializer = AccountSerializer(account)

        return Response(serializer.data, status.HTTP_200_OK)

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.models import Accounts


class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=20, validators=[UniqueValidator(queryset=Accounts.objects.all())]
    )
    email = serializers.EmailField(
        max_length=127, validators=[UniqueValidator(queryset=Accounts.objects.all())]
    )
    birthdate = serializers.DateField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    bio = serializers.CharField(allow_null=True, allow_blank=True, default=None)
    is_critic = serializers.BooleanField(allow_null=True, default=False)
    updated_at = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        newUser = Accounts.objects.create_user(**validated_data)

        return newUser


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            type=User.CUSTOMER,
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        if not check_password(validated_data.pop('password'), instance.password):
            raise serializers.ValidationError({'password': 'Current password is incorrect'})
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, max_length=128)
    new_password = serializers.CharField(required=True, max_length=128)
    confirmation = serializers.CharField(required=True, max_length=128)

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def validate_confirmation(self, value):
        validate_password(value)
        return value

    def validate(self, data):
        if data.get('new_password') != data.get('confirmation'):
            raise serializers.ValidationError({'confirmation': 'New password and confirmation do not match'})
        return data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["type"] = self.user.type

        # if api_settings.UPDATE_LAST_LOGIN:
        #     update_last_login(None, self.user)

        return data

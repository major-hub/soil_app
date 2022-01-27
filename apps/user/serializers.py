from rest_framework import serializers
from user.models import User
from main.exceptions.user_exceptions import UserException


user_exception = UserException


class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'first_name', 'last_name', 'password', 'password_confirmation']

    def validate(self, attrs):
        password_confirmation = attrs.pop('password_confirmation')
        if password_confirmation != attrs.get('password'):
            raise serializers.ValidationError({'non_field_errors': user_exception("NOT_MATCHED_PASSWORDS").message})
        return attrs


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128)


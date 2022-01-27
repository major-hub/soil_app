from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from user.serializers import UserRegisterSerializer, UserLoginSerializer
from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserViewSet(ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    login_serializer = UserLoginSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = get_user_model().objects.get(id=serializer.data['id'])
        token = get_tokens_for_user(user)
        return Response(token, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = self.login_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = get_user_model().objects.filter(email=email)
        if user.exists():
            valid_password = user.first().check_password(password)
            if valid_password:
                return Response(get_tokens_for_user(user.first()), status=status.HTTP_200_OK)
            return Response({"password": "Wrong password"})
        return Response({'email': 'User with this email does not exist'})

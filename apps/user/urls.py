from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from user.views import UserViewSet

router = routers.SimpleRouter()
router.register('user', UserViewSet, 'user')

urlpatterns = [
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/token/verify/', TokenVerifyView.as_view()),
    path('', include(router.urls))
]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from main.models import Static


class StaticAPIView(APIView):
    def get(self, request):
        data = dict()
        for item in Static.objects.all():
            data[item.key] = item.value
        return Response(data, status=status.HTTP_200_OK)



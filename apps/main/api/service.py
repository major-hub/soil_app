from rest_framework.viewsets import ModelViewSet

from main.models import Service, Function
from main.serializers.service import ServiceSerializer, FunctionSerializer


class ServiceModelViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_serializer_context(self):
        context = super(ServiceModelViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class FunctionViewSet(ModelViewSet):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer

from rest_framework.viewsets import ModelViewSet

from main.models import Laboratory
from main.serializers.laboratory import LaboratorySerializer


class LaboratoryViewSet(ModelViewSet):
    serializer_class = LaboratorySerializer
    queryset = Laboratory.objects.all()
    filter_fields = ['type', ]

    def get_serializer_context(self):
        context = super(LaboratoryViewSet, self).get_serializer_context()
        context.update({
            'request': self.request
        })
        return context

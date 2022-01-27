from rest_framework.viewsets import ModelViewSet

from main.models import Partner
from main.serializers.partner import PartnerSerializer


class PartnerViewSet(ModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()

    def get_serializer_context(self):
        context = super(PartnerViewSet, self).get_serializer_context()
        context.update({
            'request': self.request
        })
        return context

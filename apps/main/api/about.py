from rest_framework.viewsets import ModelViewSet

from main.models import History
from main.serializers.about import HistorySerializer


class HistoryViewSet(ModelViewSet):
    serializer_class = HistorySerializer
    queryset = History.objects.all()

    def get_serializer_context(self):
        context = super(HistoryViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context

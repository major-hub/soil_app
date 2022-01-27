from rest_framework.viewsets import ModelViewSet

from main.models import Document
from main.serializers.document import DocumentSerializer


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

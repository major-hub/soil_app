from rest_framework.viewsets import ModelViewSet

from main.models import Gallery, GalleryType
from main.serializers.gallery import GallerySerializer, GalleryTypeSerializer


class GalleryViewSet(ModelViewSet):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()

    def get_serializer_context(self):
        context = super(GalleryViewSet, self).get_serializer_context()
        context.update({
            'request': self.request
        })
        return context


class GalleryTpeViewSet(ModelViewSet):
    serializer_class = GalleryTypeSerializer
    queryset = GalleryType.objects.all()

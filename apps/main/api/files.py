from django.db.models import ProtectedError
from django.utils.translation import gettext as _

# Rest Framework
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

# Project
from main.models import File
from main.serializers.files import FileSerializer, ImageField


class FileViewSet(viewsets.ModelViewSet):
    model = File
    queryset = File.objects.all()
    serializer_class = FileSerializer

    search_fields = ('name',)
    ordering_fields = ('name', 'create_date',)

    def get_queryset(self):
        return self.model.objects.all()

    def pre_save(self, obj):
        obj.file = self.request.FILES.get('file')

    def destroy(self, request, *args, **kwargs):
        try:
            return super(FileViewSet, self).destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(data={_('This object can not be deleted')}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        thumbnail = request.GET.get('thumbnail_type', None)
        instance = self.get_object()
        if thumbnail:
            ctx = dict()
            ctx['request'] = request
            serializer = ImageField(ctx=ctx)
            return Response(serializer.to_representation(instance))
        else:
            return super(FileViewSet, self).retrieve(request, *args, **kwargs)

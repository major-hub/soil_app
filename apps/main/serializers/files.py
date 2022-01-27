from rest_framework import serializers

from main.models import File
from easy_thumbnails.files import get_thumbnailer


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'name', 'file')


class ThumbnailSerializer(serializers.ImageField):
    """
    Allows to choose ImageField size.
    Options: small, medium, large
    Default value: small
    """

    def __init__(self, *args, ctx=None, **kwargs):
        super(ThumbnailSerializer, self).__init__(*args, **kwargs)
        self.size = 'original'
        if ctx and hasattr(ctx.get('request'), 'GET'):
            self.size = ctx.get('request').GET.get('thumbnail_type', self.size)
            self.request = ctx.get('request')

    def to_representation(self, value):
        if self.size == 'original':
            url = value.url
        else:
            url = get_thumbnailer(value)[self.size].url
        return self.request.build_absolute_uri(url)


class FileSizedSerializer(serializers.ModelSerializer):
    file = ThumbnailSerializer()

    class Meta:
        model = File
        fields = ('id', 'name', 'file',)

    def __init__(self, *args, ctx=None, **kwargs):
        super(FileSizedSerializer, self).__init__(*args, **kwargs)
        if ctx:
            self.fields['file'] = ThumbnailSerializer(ctx=ctx)


class ImageField(serializers.PrimaryKeyRelatedField):
    def __init__(self, ctx=None, **kwargs):
        super(ImageField, self).__init__(**kwargs)
        self.ctx = ctx

    def get_queryset(self):
        return File.objects.all()

    def to_representation(self, value):
        pk = value if type(value) is int else value.pk
        file = File.objects.get(pk=pk)
        serializer = FileSizedSerializer(file, ctx=self.ctx)
        return serializer.data

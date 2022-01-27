from rest_framework import serializers

from main.models import Gallery, GalleryType
from main.serializers.files import FileSerializer


class GalleryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryType
        exclude = []


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        exclude = ['created_date', 'updated_date']
        
    def to_representation(self, instance):
        self.fields['image'] = FileSerializer(instance.image, context=self.context)
        self.fields['video'] = FileSerializer(instance.video, context=self.context)
        self.fields['type'] = GalleryTypeSerializer(instance.type)
        return super(GallerySerializer, self).to_representation(instance)
from rest_framework import serializers

from main.models import Document, DocumentImages, File
from main.serializers.files import FileSerializer


class DocumentSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(queryset=File.objects.all(), allow_null=True, required=False, many=True,
                                                write_only=True)

    class Meta:
        model = Document
        exclude = []

    def create(self, validated_data):
        images = validated_data.pop('images', None)
        document = Document.objects.create(**validated_data)
        document_images = [DocumentImages(document=document, image=image) for image in images]
        DocumentImages.objects.bulk_create(document_images)
        return document

    def update(self, instance, validated_data):
        images = validated_data.pop('images', None)
        instance.documentimages_set.all().delete()
        if images:
            document_images = [DocumentImages(document=instance, image=image) for image in images]
            DocumentImages.objects.bulk_create(document_images)
        return super(DocumentSerializer, self).update(instance, validated_data)

    def to_representation(self, instance):
        data = super(DocumentSerializer, self).to_representation(instance)
        image_ids = instance.documentimages_set.all().values_list('image', flat=True)
        images = File.objects.filter(id__in=image_ids)
        data.update({'images': FileSerializer(images, many=True, context=self.context).data})
        return data

from rest_framework import serializers

from main.models import Laboratory, LaboratoryImage, File
from main.serializers.files import FileSerializer


class LaboratorySerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(queryset=File.objects.all(), required=False, allow_null=True, many=True,
                                                write_only=True)
    
    class Meta:
        model = Laboratory
        exclude = []

    def create(self, validated_data):
        images = validated_data.pop('images', None)    
        laboratory = Laboratory.objects.create(**validated_data)
        if images:
            data = [LaboratoryImage(laboratory=laboratory, image=image) for image in images]
            LaboratoryImage.objects.bulk_create(data)
        return laboratory
    
    def update(self, instance, validated_data):
        images = validated_data.pop('images', None)
        instance.laboratoryimage_set.all().delete()
        if images:
            data = [LaboratoryImage(laboratory=instance, image=images) for image in images]
            LaboratoryImage.objects.bulk_create(data)
        return super(LaboratorySerializer, self).update(instance, validated_data)
    
    def to_representation(self, instance):
        data = super(LaboratorySerializer, self).to_representation(instance)
        image_ids = instance.laboratoryimage_set.all().values_list('image', flat=True)
        images = File.objects.filter(id__in=image_ids)
        data.update({'images': FileSerializer(images, many=True, context=self.context).data})
        return data

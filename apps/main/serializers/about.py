from rest_framework import serializers

from main.models import History, HistoryImages, File
from main.serializers.files import FileSerializer


class HistoryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryImages
        exclude = []


class HistorySerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(queryset=File.objects.all(), required=False, allow_null=True, many=True,
                                                write_only=True)

    class Meta:
        model = History
        exclude = []

    def create(self, validated_data):
        images = validated_data.pop('images', None)
        history_obj = History.objects.create(**validated_data)
        if images:
            data = [HistoryImages(image=image, history=history_obj) for image in images]
            HistoryImages.objects.bulk_create(data)
        return history_obj

    def update(self, instance, validated_data):
        instance.historyimages_set.all().delete()
        images = validated_data.pop('images', None)
        if images:
            data = [HistoryImages(image=image, history_id=instance.id) for image in images]
            HistoryImages.objects.bulk_create(data)
        return super(HistorySerializer, self).update(instance, validated_data)

    def to_representation(self, instance):
        data = super(HistorySerializer, self).to_representation(instance)
        image_ids = instance.historyimages_set.all().values_list('image', flat=True)
        images = File.objects.filter(id__in=image_ids)
        data.update({'images': FileSerializer(images, many=True, context=self.context).data})
        return data

from rest_framework import serializers
from django.utils.translation import gettext as _

from main.models import News, NewsImage, File
from main.serializers.files import FileSerializer


class NewsSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(queryset=File.objects.all(), required=False, allow_null=True, many=True,
                                                write_only=True)

    class Meta:
        model = News
        exclude = []

    def create(self, validated_data):
        images = validated_data.pop('images', None)
        news = News.objects.create(**validated_data)
        if images:
            data = [NewsImage(news=news, image=image) for image in images]
            NewsImage.objects.bulk_create(data)
        return news

    def update(self, instance, validated_data):
        views_count = validated_data.get('view_count', None)
        if views_count:
            raise serializers.ValidationError(detail=_('Views count can not be upgraded'))
        images = validated_data.pop('images', None)
        instance.newsimage_set.all().delete()
        if images:
            data = [NewsImage(news=instance, image=image) for image in images]
            NewsImage.objects.bulk_create(data)
        return super(NewsSerializer, self).update(instance, validated_data)

    def to_representation(self, instance):
        data = super(NewsSerializer, self).to_representation(instance)
        image_ids = instance.newsimage_set.all().values_list('image', flat=True)
        images = File.objects.filter(id__in=image_ids)
        data.update({'images': FileSerializer(images, many=True, context=self.context).data})
        return data

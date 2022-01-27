from rest_framework import serializers

from main.models import Service, ServiceImages, File, Function
from main.serializers.files import FileSerializer


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['image']
        model = ServiceImages

    def to_representation(self, instance):
        self.fields['image'] = FileSerializer(instance.image, context=self.context)
        return super(ServiceImageSerializer, self).to_representation(instance)


class ServiceSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(queryset=File.objects.all(), required=False, allow_null=True, many=True,
                                                write_only=True)

    class Meta:
        model = Service
        fields = '__all__'

    def create(self, validated_data):
        images = validated_data.pop('images')
        service = Service.objects.create(**validated_data)
        service_images = [ServiceImages(service=service, image=image) for image in images]
        ServiceImages.objects.bulk_create(service_images)
        return service

    def update(self, instance, validated_data):
        images = validated_data.pop('images', None)
        instance.serviceimages_set.all().delete()
        if images:
            service_images = [ServiceImages(service=instance, image=image) for image in images]
            ServiceImages.objects.bulk_create(service_images)
        return super(ServiceSerializer, self).update(instance, validated_data)

    def to_representation(self, instance):
        data = super(ServiceSerializer, self).to_representation(instance)
        image_ids = instance.serviceimages_set.all().values_list('image', flat=True)
        images = File.objects.filter(id__in=image_ids)
        data.update({'images': FileSerializer(images, many=True, context=self.context).data})
        return data


class FunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = '__all__'

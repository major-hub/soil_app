from rest_framework import serializers

from main.models import Partner
from main.serializers.files import FileSerializer


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
        
    def to_representation(self, instance):
        self.fields['logo'] = FileSerializer(instance.logo, context=self.context)
        return super(PartnerSerializer, self).to_representation(instance)
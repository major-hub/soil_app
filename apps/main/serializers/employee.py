from rest_framework import serializers

from main.models import Employee
from main.serializers.files import FileSerializer


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        exclude = ['created_date', 'updated_date']

    def to_representation(self, instance):
        self.fields['image'] = FileSerializer(data=instance.image, context=self.context)
        return super(EmployeeSerializer, self).to_representation(instance)

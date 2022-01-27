from rest_framework import serializers

from main.models import Static


class StaticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Static
        fields = '__all__'

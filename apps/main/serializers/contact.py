from rest_framework import serializers
from main.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ['created_date', 'updated_date']

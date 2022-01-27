from rest_framework.generics import ListCreateAPIView
from main.models import Contact
from main.serializers.contact import ContactSerializer


class ContactApiView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    search_fields = ['full_name', ]
    ordering_fields = ['created_date', ]

from django.db import models
from django.utils.translation import gettext as _
from main.models import BaseModel


class Contact(BaseModel):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    phone_number = models.CharField(max_length=17)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

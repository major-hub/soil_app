from django.db import models
from django.utils.translation import gettext as _

from main.models import BaseModel
from main.models import File


class Employee(BaseModel):
    full_name = models.CharField(max_length=255)
    image = models.ForeignKey(File, on_delete=models.SET_NULL, null=True)
    about = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True)
    time_to_apply = models.CharField(max_length=150, blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def __str__(self):
        return self.full_name

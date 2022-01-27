from django.db import models
from django.utils.translation import gettext as _

from main.models import BaseModel
from main.models import File


class Employee(BaseModel):
    full_name = models.CharField(max_length=255)
    image = models.ForeignKey(File, on_delete=models.SET_NULL, null=True)
    about = models.TextField()

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def __str__(self):
        return self.full_name

from django.db import models
from django.utils.translation import gettext as _

from main.models import BaseModel


class Partner(BaseModel):
    name = models.CharField(max_length=50)
    logo = models.ForeignKey('main.File', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _("Partners")

    def __str__(self):
        return self.name

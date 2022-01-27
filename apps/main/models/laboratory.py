from django.db import models
from django.utils.translation import gettext as _

from main.models import BaseModel


class Laboratory(BaseModel):
    TYPE = (
        ('mobile', 'mobile'),
        ('static', 'static'),
    )
    name = models.CharField(max_length=255)
    body = models.TextField()
    type = models.CharField(max_length=6, choices=TYPE)

    class Meta:
        verbose_name = _('Laboratory')
        verbose_name_plural = _('Laboratories')

    def __str__(self):
        return self.name


class LaboratoryImage(models.Model):
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    image = models.ForeignKey('main.File', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Laboratory Image')
        verbose_name_plural = _('Laboratory Images')

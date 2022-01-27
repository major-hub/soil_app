from django.db import models
from django.utils.translation import gettext as _

from main.models import BaseModel


class Service(BaseModel):
    name = models.CharField(max_length=255)
    about = models.TextField()

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name


class ServiceImages(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ForeignKey('main.File', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Service Image')
        verbose_name_plural = _("Service Images")


class Function(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        verbose_name = _('Function')
        verbose_name_plural = _("Functions")

    def __str__(self):
        return self.title

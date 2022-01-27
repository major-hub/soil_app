from django.db import models
from django.utils.translation import gettext as _

from main.models import BaseModel


class Document(BaseModel):
    name = models.CharField(max_length=255)
    link1 = models.URLField(null=True, blank=True)
    link2 = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')

    def __str__(self):
        return self.name


class DocumentImages(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    image = models.ForeignKey('main.File', on_delete=models.CASCADE)

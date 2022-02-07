from django.db import models
from django.utils.translation import gettext as _
from main.models import BaseModel


class GalleryType(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Gallery Type')
        verbose_name_plural = _('Gallery Types')

    def __str__(self):
        return self.title


class Gallery(BaseModel):
    image = models.ForeignKey('main.File', on_delete=models.CASCADE, null=True, blank=True, related_name='image')
    video = models.URLField(null=True, blank=True)
    type = models.ForeignKey(GalleryType, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')

    def __str__(self):
        return self.type.title

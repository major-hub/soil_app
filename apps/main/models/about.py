from django.db import models
from django.utils.translation import gettext as _

from main.models import File, BaseModel


class History(BaseModel):
    text = models.TextField()

    class Meta:
        verbose_name = _('History')
        verbose_name_plural = _('Histories')

    def __str__(self):
        return self.text


class HistoryImages(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    image = models.ForeignKey(File, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('History Image')
        verbose_name_plural = _('History Images')

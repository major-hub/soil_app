from django.db import models
from django.utils.translation import gettext as _
from main.models import BaseModel


class News(BaseModel):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    body = models.TextField()
    view_count = models.IntegerField(default=0)
    video = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _("News")

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ForeignKey('main.File', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('News Image')
        verbose_name_plural = _("News Images")

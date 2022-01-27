import datetime
import uuid

from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import ValidationError as Error
from django.utils.translation import gettext as _

from rest_framework.serializers import ValidationError

FILE_TYPES = {
    r'^(doc|docx)$': 'document',
    r'^(pdf)$': 'pdf',
    r'^(jpg|jpeg|png|gif)$': 'image',
    r'^(xls|xlsx)$': 'excel',
    r'^(zip|rar)$': 'compressed',
    r'^(mp4|avi|flv)$': 'video',
}


def upload_name(instance, filename):
    file_type = filename.split('.')[-1]
    today = str(datetime.datetime.today())[0:7]
    for regex, folder in FILE_TYPES.items():
        try:
            RegexValidator(regex).__call__(file_type)
            return 'file/%s/%s/%s.%s' % (
                folder, today, uuid.uuid4(), file_type
            )
        except Error:
            pass
    raise ValidationError(detail={_('File type is unacceptable')})


class File(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to=upload_name)

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')

    def __str__(self):
        return self.name or f'id={self.id}'

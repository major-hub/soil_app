from django.db import models
from main.managers.base_manager import BaseManager


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DeleteMixin(models.Model):
    is_deleted = models.BooleanField(default=False)

    objects = BaseManager()
    raw_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

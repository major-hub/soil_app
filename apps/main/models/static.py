from django.db import models


class Static(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.key}-{self.value}'
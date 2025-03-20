from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    iso_code = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name
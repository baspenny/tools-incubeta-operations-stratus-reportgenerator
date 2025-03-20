from django.db import models

from app.models.country import Country


class Client(models.Model):
    name = models.CharField(max_length=255, unique=False)
    acumatica_code = models.CharField(max_length=255, unique=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    creamos_client_id = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.name} ({self.acumatica_code})"

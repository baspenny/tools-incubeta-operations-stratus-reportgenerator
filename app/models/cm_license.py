from django.db import models

class CmLicense(models.Model):
    client = models.ForeignKey("Client", on_delete=models.RESTRICT)
    account_id = models.IntegerField()
    profile_id = models.IntegerField()
    report_id = models.IntegerField()
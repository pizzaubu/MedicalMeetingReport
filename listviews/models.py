from django.db import models


class Report(models.Model):
    header = models.CharField(max_length=20)
    report_id = models.CharField(max_length=20)
    file = models.FileField(upload_to='reports/')

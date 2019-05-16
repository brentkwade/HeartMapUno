from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class Scan(models.Model):
    title = models.CharField(max_length=100)
    csv = models.FileField(upload_to='scans/csvs/')

    def __str__(self):
        return self.title

from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


class DataExtraction(models.Model):
    dataset = JSONField(blank=True, null=True)

    def __str__(self):
        return self.name


class Extraction(models.Model):
    name = models.CharField(max_length=100, blank=False, default=None)
    created_date = models.DateTimeField(default=timezone.now)
    lawsuits = models.FileField(blank=True, null=False)
    customer = models.CharField(max_length=100, blank=False, default=None)
    result = models.FileField(blank=True, null=True)
    total_lawsuits = models.CharField(
        max_length=100, null=True, blank=True, default=None)
    found = models.CharField(
        max_length=100, null=True, blank=True, default=None)
    status = models.CharField(
        max_length=100, null=True, blank=True, default=None)

    def __str__(self):
        return self.name

    def save(self):
        self.total_lawsuits = sum(1 for line in self.lawsuits.read())
        super(Extraction, self).save()

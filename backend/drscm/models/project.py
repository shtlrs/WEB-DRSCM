from django.db import models
from uuid import uuid4
from .client import Client


class Project(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=150)
    hourly_rate = models.FloatField()
    travel_hourly_rate = models.FloatField()
    travel_fixed_rate = models.FloatField()
    currency = models.CharField(max_length=10)

    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)



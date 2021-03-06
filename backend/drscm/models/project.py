from django.db import models
from uuid import uuid4
from .client import Client


class Project(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=150)
    hourly_rate = models.FloatField(null=False, blank=False, default=175)
    travel_hourly_rate = models.FloatField(null=True, default=0, blank=True)
    travel_fixed_rate = models.FloatField(null=True, default=0, blank=True)
    currency = models.CharField(max_length=10)
    owner = models.ForeignKey(to="User", related_name="projects", on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, related_name="projects", on_delete=models.CASCADE)

    def __str__(self):
        return f"Project: {self.name}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.owner = self.client.owner
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

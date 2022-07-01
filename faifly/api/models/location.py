from django.db import models


class Location(models.Model):

    nameLocation = models.CharField(max_length=100, verbose_name="Location name", blank=True)

    class Meta:
        verbose_name = "Location name"

    def __str__(self):
        return self.nameLocation


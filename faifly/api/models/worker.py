from django.db import models

from api.models import location


class Worker(models.Model):

    full_name = models.CharField(max_length=140, verbose_name='Worker name')
    # work_location = models.OneToOneField(
    #     to=location.Location,
    #     verbose_name="Location of work",
    #     related_name="location",
    #     on_delete=models.PROTECT,
    #     null=True,
    #     blank=True,
    # )

    def __str__(self):
        return self.full_name
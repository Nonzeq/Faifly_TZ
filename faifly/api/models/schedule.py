from django.db import models
from django import forms

from api.models import days, worker, location
from django.core.exceptions import ValidationError
from rest_framework import serializers
import datetime
from api.models.location import Location


class Schedule(models.Model):
    worker = models.ForeignKey(
        to=worker.Worker,
        verbose_name="schedule to worker",
        related_name="worker_schedule",
        on_delete=models.PROTECT,
        default=None
    )
    work_day = models.CharField(max_length=30, verbose_name="Day", choices=days.Days.choices, default=None)
    time_start = models.TimeField(verbose_name="Start work", null=True,)
    time_end = models.TimeField(verbose_name="End work", null=True)
    is_update = models.BooleanField(default=False)
    work_location = models.ManyToManyField(
        location.Location,
        verbose_name="Location of work",
        related_name="location",
        # on_delete=models.CASCADE,
        # null=True,
        blank=True,
    )
    def get_work_location(self):
        return "\n".join([p.nameLocation for p in self.work_location.all()])

    def save(self, *args, **kwargs):

        if self.is_update == False:
            queryset = Schedule.objects.filter(
                work_day=self.work_day,
            )
            # queryset_day = Schedule.objects.filter(time__range=(self.time_start, self.time_end))
            # for i in queryset_day:
            #     print(i.work_location)
            for item in queryset:
                if item.time_start <= (self.time_start or self.time_end) <= item.time_end:
                    raise forms.ValidationError(
                        message=f"this time has already exist {self.time_start}-{self.time_end}"
                    )
                elif self.time_start <= item.time_start and self.time_end >= item.time_end:
                    raise ValidationError(f"Top range time error")


        super().save(*args, **kwargs)


    class Meta:
        ordering = ['time_start']
        # unique_together = ('work_location', 'work_day')



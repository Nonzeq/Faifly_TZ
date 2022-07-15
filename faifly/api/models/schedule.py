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
    work_location = models.ForeignKey(
        location.Location,
        verbose_name="Location of work",
        related_name="location",
        blank=True,
        on_delete=models.CASCADE,
    )

    def _is_instance(self, pk) -> bool:

        if self.pk == pk:
            return True
        return False


    def clean(self):

        for item in Schedule.objects.filter(
            work_location=self.work_location,
            work_day=self.work_day,
                                            ):
            worker, location, day, start, end = \
                item.worker, item.work_location, item.work_day, item.time_start, item.time_end
            print(worker, location, day, start, end)
            if not self._is_instance(item.pk):
                if start < self.time_start < end or start < self.time_end < end:
                    raise ValidationError(
                        {'time_start': f" Day {self.work_day} in loc {self.work_location} "
                            f"this time range has already exist {self.time_start} worker - {worker}",
                        'time_end': f"Day {self.work_day}  in loc {self.work_location}"
                            f"in this time range has already exist {self.time_end} worker - {worker}"},
                        )
                if self.time_start < start < self.time_end or self.time_start < end < self.time_end:
                    raise ValidationError(
                        {'time_start': f" Day {self.work_day} in loc {self.work_location} "
                                       f"in this time range has shedule {start}-{end} worker - {worker}",
                        'time_end': f"Day {self.work_day}  in loc {self.work_location}"
                                     f"in this time range has has shedule {start}-{end} worker - {worker}"},
                    )



    class Meta:
        ordering = ['time_start']









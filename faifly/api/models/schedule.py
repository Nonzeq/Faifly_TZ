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
    # def get_work_location(self):
    #     return "\n".join([p.nameLocation for p in self.work_location.all()])



    def save(self, *args, **kwargs):

        if self.is_update == False:
            queryset = Schedule.objects.filter(
                worker=self.worker,
                work_day=self.work_day,
                work_location=self.work_location,
            )
            print([i.worker for i in queryset])
            for schedule_time in queryset:
                if schedule_time.time_start < self.time_start < schedule_time.time_end or \
                        schedule_time.time_start < self.time_end < schedule_time.time_end:
                    raise forms.ValidationError(
                        message=f"this time range has already exist {self.time_start}-{self.time_end}"
                    )
                else:
                    if self.time_start < schedule_time.time_start < self.time_end or \
                            self.time_start < schedule_time.time_end < self.time_end:
                        raise forms.ValidationError(
                            message=f"this  time {self.worker} has Schedule, your time: {self.time_start}-{self.time_end}"
                                    f" exist time: {schedule_time.time_start}-{schedule_time.time_end}"
                        )

        super().save(*args, **kwargs)


    class Meta:
        ordering = ['time_start']
        # unique_together = ('work_location', 'work_day')



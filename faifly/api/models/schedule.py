from django.db import models
from api.models import days, worker
from django.core.exceptions import ValidationError



class Schedule(models.Model):
    worker = models.ForeignKey(
        to=worker.Worker,
        verbose_name="schedule to worker",
        related_name="worker_schedule",
        on_delete=models.PROTECT,
        default=None
    )
    work_day = models.CharField(max_length=30, verbose_name="Day", choices=days.Days.choices, default=None)
    time_start = models.TimeField(verbose_name="Start work", null=True)
    time_end = models.TimeField(verbose_name="End work", null=True)

    def save(self, *args, **kwargs):

        queryset = Schedule.objects.filter(worker=self.worker, work_day=self.work_day)
        for item in queryset:
            if item.time_start <= (self.time_start or self.time_end) <= item.time_end:
                raise ValidationError(f"this time has already exist {self.time_start}-{self.time_end}")
            elif self.time_start <= item.time_start and self.time_end >= item.time_end:
                raise ValidationError(f"Top range time error")
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['time_start']

from django.db import models
from rest_framework import serializers

from api.models import worker
from api.models.model_custom_validators import date_now_validator, validate_on_schedule_time, \
    validate_on_appointment_time
from api.models.schedule import Schedule
from api.tools import getDay
from users.models import User


class Appointment(models.Model):

    apointment_worker = models.ForeignKey(
        to=worker.Worker,
        related_name="apointment_worker",
        verbose_name="worker to apointment",
        on_delete=models.PROTECT,
    )
    date = models.DateField(verbose_name="Apointment date", validators=[date_now_validator])
    apointment_start = models.TimeField(verbose_name="Apointment time start",)
    apointment_end = models.TimeField(verbose_name="Apointment time end")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user')

    def save(self,*args, **kwargs):
        day = getDay(self.date)
        queryset_schedule = Schedule.objects.filter(worker=self.apointment_worker, work_day=day)
        queryset_appointment = Appointment.objects.filter(date=self.date, apointment_worker=self.apointment_worker)
        for range_time in queryset_appointment:
            if range_time.apointment_start < self.apointment_start < range_time.apointment_end or \
                    range_time.apointment_start < self.apointment_end < range_time.apointment_end:
                raise serializers.ValidationError(
                    f'this time {self.apointment_start}-{self.apointment_end} already exist')
            else:
                if self.apointment_start < range_time.apointment_start < self.apointment_end or \
                        self.apointment_start < range_time.apointment_end < self.apointment_end:
                    raise serializers.ValidationError(
                        f'In this time range '
                        f'{self.apointment_start}-{self.apointment_end} {self.apointment_worker} has appointment'
                    )
        if queryset_schedule:
            for schedule_time in queryset_schedule:
                if schedule_time.time_start <= self.apointment_start <= schedule_time.time_end and \
                        schedule_time.time_start <= self.apointment_end <= schedule_time.time_end:
                    super().save(*args, **kwargs)
                else:
                    raise serializers.ValidationError(
                        f"For worker {self.apointment_worker} range time on {day} "
                        f"{list((str(schedule_time.time_start), str(schedule_time.time_end)) for i in queryset_schedule)}"
                    )
        else:
            raise serializers.ValidationError(f"{self.apointment_worker} doesn't working on {day}")

        # validate_on_schedule_time(
        #     queryset_schedule,
        #     self.apointment_start,
        #     self.apointment_end,
        #     self.apointment_worker,
        #     day
        # )
        # validate_on_appointment_time(queryset_appointment, self.apointment_start, self.apointment_end,self.date)
        super().save(*args, **kwargs)
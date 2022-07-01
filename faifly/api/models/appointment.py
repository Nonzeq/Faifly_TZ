from django.core.exceptions import ValidationError
from django.db import models
from api.models import worker
from api.models.model_custom_validators import date_now_validator, validate_on_schedule_time, \
    validate_on_appointment_time
from api.models.schedule import Schedule
from api.tools import getDay


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

    def save(self,*args, **kwargs):
        day = getDay(self.date)
        queryset_schedule = Schedule.objects.filter(worker=self.apointment_worker, work_day=day)
        queryset_appointment = Appointment.objects.filter(apointment_worker=self.apointment_worker)
        validate_on_schedule_time(
            queryset_schedule,
            self.apointment_start,
            self.apointment_end,
            self.apointment_worker,
            day
        )
        validate_on_appointment_time(queryset_appointment, self.apointment_start, self.apointment_end,self.date)
        super().save(*args, **kwargs)
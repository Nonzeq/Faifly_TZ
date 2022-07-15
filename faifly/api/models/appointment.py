from django.core.exceptions import ValidationError
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
    class Meta:
        ordering = ['apointment_start']

    def _time_to_int(self, time:str) -> int:
        hh, mm, ss = map(int, time.split(':'))
        return ss + 60*(mm + 60*hh)

    def _min_range_time_appointment(self, start, end):
        start = self._time_to_int(str(start))
        end = self._time_to_int(str(end))
        if (end - start) // 60 < 30:
            raise serializers.ValidationError(
                f'{self.apointment_start} {self.apointment_end} minimal appointment time must be 30 minutes '
            )

    def _is_instance(self, pk) -> bool:

        if self.pk == pk:
            return True
        return False

    def save(self, *args, **kwargs):
        day = getDay(self.date)
        self._min_range_time_appointment(self.apointment_start, self.apointment_end)
        if self.apointment_start == self.apointment_end:
            raise serializers.ValidationError(
               f'{self.apointment_start} cannot be equal to {self.apointment_end}'
            )
        message_time_error = []
        for item in Schedule.objects.select_related('worker').filter(worker=self.apointment_worker, work_day=day):
            worker, location, day, start, end = \
                item.worker, item.work_location, item.work_day, item.time_start, item.time_end
            if start <= self.apointment_start <= end and start <= self.apointment_end <= end:
                message_time_error = []
                break
            else:
                message_time_error.append(str(start) + '-' + str(end))
        # else:
        #     raise serializers.ValidationError(
        #         f"This date {self.date}, {getDay(self.date)}, {self.apointment_worker} don't working"
        #     )

        if message_time_error:
            raise serializers.ValidationError(
                 f"Worker {worker}, time range on {day} is {message_time_error}"
            )

        for item in Appointment.objects.filter(
            apointment_worker=self.apointment_worker,
            date=self.date
        ):
            worker, date, start, end = item.apointment_worker, item.date, item.apointment_start, item.apointment_end
            if not self._is_instance(item.pk):
                if start <= self.apointment_start <= end and start <= self.apointment_end <= end:
                    raise serializers.ValidationError(
                         f"Worker {worker}, "
                                             f"time range on {day} "
                                             f"time {self.apointment_start}-{self.apointment_end} is exist "
                                             f"worker has appointment {start}-{end}"
                    )
                elif self.apointment_start < start < self.apointment_end or \
                        self.apointment_start < end < self.apointment_end:
                    raise serializers.ValidationError(
                         f"Worker {worker}, "
                                             f"in this time {self.apointment_start}-{self.apointment_end}"
                                             f" has appointment "
                                             f"sience {start} to {end}"
                    )
        super().save(*args, **kwargs)




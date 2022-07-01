from django.core.exceptions import ValidationError # or APIExeptions
from django.utils.timezone import now
from api.models.schedule import Schedule



def date_now_validator(date):
    today = now().date()
    if date < today:
        raise ValidationError(f"Неправильная дата: {date}")


def validate_on_schedule_time(queryset, apointment_start, apointment_end, apointment_worker, day):
    """validate for schedule time range"""
    if queryset:
        for item in queryset:
            if apointment_start < item.time_start or apointment_end > item.time_end:
                raise ValidationError(
                    f"For worker {apointment_worker} range time on {day} "
                    f"{list((str(i.time_start), str(i.time_end)) for i in queryset)}"
                )
    else:
        raise ValidationError(f"{apointment_worker} don't working on {day}")


def validate_on_appointment_time(queryset, apointment_start, apointment_end, date):
    """validate for appointment """
    for item in queryset:
        if item.date == date:
            if item.apointment_start <= (apointment_start or apointment_end) <= item.apointment_end:
                raise ValidationError(f"this time appointment: {apointment_start}-{apointment_end} already exist")

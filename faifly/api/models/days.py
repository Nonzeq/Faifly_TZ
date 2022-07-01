from django.db import models


class Days(models.TextChoices):
    MONDAY = "MONDAY", "Понедельник"
    TUESDAY = "TUESDAY", "Вторник"
    WEDNESDAY = "WEDNESDAY", "Среда"
    THURSDAY = "THURSDAY", "Четверг"
    FRIDAY = "FRIDAY", "Пятница"
    SATURDAY = "SATURDAY", "Суббота"
    SUNDAY = "SUNDAY", "Воскресенье"
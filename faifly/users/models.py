from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Roles(models.TextChoices):
    CUSTOMER = "CUSTOMER", "Клиент"
    WORKER = "WORKER", "Рабочий"


class User(AbstractUser):
    first_name = models.CharField(max_length=155, verbose_name="First name",)
    last_name = models.CharField(max_length=155, verbose_name="Last name")
    email = models.EmailField(unique=True, verbose_name="Email")
    role = models.CharField(max_length=30, choices=Roles.choices)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.first_name

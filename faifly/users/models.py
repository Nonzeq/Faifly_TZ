from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from api.models.worker import Worker


class Roles(models.TextChoices):
    CUSTOMER = "CUSTOMER", "Клиент"
    WORKER = "WORKER", "Рабочий"


class User(AbstractUser):
    first_name = models.CharField(max_length=155, verbose_name="First name", blank=True)
    last_name = models.CharField(max_length=155, verbose_name="Last name", blank=True)
    email = models.EmailField(unique=True, verbose_name="Email")
    role = models.CharField(max_length=30, choices=Roles.choices)
    worker = models.OneToOneField(Worker, default=None, blank=True, null=True, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    # def save(self, *args, **kwargs):
    #     print('1')
    #     if self.role == Roles.WORKER:
    #         self.worker = Worker.objects.create(
    #             full_name=self.email
    #         )
    #     super().save(*args, **kwargs)
    def __str__(self):
        return self.email

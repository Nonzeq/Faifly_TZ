# Generated by Django 4.0.5 on 2022-06-30 10:50

import api.models.model_custom_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_alter_schedule_work_day'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['time_start']},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(validators=[api.models.model_custom_validators.date_now_validator], verbose_name='Apointment date'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_remove_apointment_range_time_delete_timerange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apointment',
            name='time_end',
            field=models.TimeField(verbose_name='end'),
        ),
        migrations.AlterField(
            model_name='apointment',
            name='time_start',
            field=models.TimeField(verbose_name='start'),
        ),
    ]

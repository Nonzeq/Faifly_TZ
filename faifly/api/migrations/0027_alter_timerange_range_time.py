# Generated by Django 4.0.5 on 2022-06-26 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_apointment_range_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timerange',
            name='range_time',
            field=models.TimeField(default=None, verbose_name='range'),
        ),
    ]

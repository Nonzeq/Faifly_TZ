# Generated by Django 4.0.5 on 2022-06-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_timerange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timerange',
            name='range_time',
            field=models.TimeField(verbose_name='range'),
        ),
    ]

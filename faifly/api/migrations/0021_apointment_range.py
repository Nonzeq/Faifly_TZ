# Generated by Django 4.0.5 on 2022-06-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_apointment_time_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apointment',
            name='range',
            field=models.TimeField(default=None, verbose_name=[models.TimeField(unique=True, verbose_name='start'), models.TimeField(unique=True, verbose_name='end')]),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-01 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0059_alter_schedule_work_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='work_location',
        ),
        migrations.AddField(
            model_name='schedule',
            name='work_location',
            field=models.ManyToManyField(blank=True, null=True, related_name='location', to='api.location', verbose_name='Location of work'),
        ),
    ]

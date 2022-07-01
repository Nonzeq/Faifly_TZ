# Generated by Django 4.0.5 on 2022-06-26 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_alter_schedule_day_alter_schedule_end_time_of_work_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='day',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(unique=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='time',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.schedule', verbose_name='Time of work'),
        ),
    ]
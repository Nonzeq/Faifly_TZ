# Generated by Django 4.0.5 on 2022-06-26 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_schedule_time_of_work_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='worker_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='api.worker', verbose_name='Time of work'),
        ),
    ]
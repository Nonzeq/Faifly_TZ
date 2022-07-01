# Generated by Django 4.0.5 on 2022-06-26 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_worker_time_of_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='time_of_work',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.schedule', verbose_name='time of work'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-26 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_remove_schedule_day_workday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='time',
        ),
        migrations.AddField(
            model_name='schedule',
            name='day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Thusday', 'Thusday'), ('Wendsday', 'Wendsday'), ('Thersday', 'Thersday'), ('Friday', 'Friday'), ('Seterday', 'Seterday')], default=None, max_length=8),
        ),
        migrations.AddField(
            model_name='schedule',
            name='person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.worker', verbose_name='Worker'),
        ),
        migrations.DeleteModel(
            name='WorkDay',
        ),
    ]

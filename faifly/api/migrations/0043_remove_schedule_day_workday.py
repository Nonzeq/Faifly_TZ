# Generated by Django 4.0.5 on 2022-06-26 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_remove_worker_day_schedule_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='day',
        ),
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Thusday', 'Thusday'), ('Wendsday', 'Wendsday'), ('Thersday', 'Thersday'), ('Friday', 'Friday'), ('Seterday', 'Seterday')], max_length=8)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.worker', verbose_name='Worker')),
            ],
        ),
    ]

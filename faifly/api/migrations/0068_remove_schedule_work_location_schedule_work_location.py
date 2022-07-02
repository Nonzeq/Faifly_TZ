# Generated by Django 4.0.5 on 2022-07-02 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0067_alter_schedule_work_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='work_location',
        ),
        migrations.AddField(
            model_name='schedule',
            name='work_location',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='api.location', verbose_name='Location of work'),
            preserve_default=False,
        ),
    ]

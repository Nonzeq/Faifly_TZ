# Generated by Django 4.0.5 on 2022-07-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0071_alter_schedule_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['time_start']},
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='work_time',
        ),
        migrations.AddField(
            model_name='schedule',
            name='time_end',
            field=models.TimeField(null=True, verbose_name='End work'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='time_start',
            field=models.TimeField(null=True, verbose_name='Start work'),
        ),
        migrations.DeleteModel(
            name='WorkTime',
        ),
    ]

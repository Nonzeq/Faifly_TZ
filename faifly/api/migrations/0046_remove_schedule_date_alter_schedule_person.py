# Generated by Django 4.0.5 on 2022-06-26 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_alter_schedule_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='date',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.worker', verbose_name='Worker'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-26 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_remove_worker_day_delete_workday'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='day',
            field=models.CharField(blank=True, default=None, max_length=255, verbose_name='Day'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_worker_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='day',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Day'),
        ),
    ]
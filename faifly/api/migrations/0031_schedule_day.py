# Generated by Django 4.0.5 on 2022-06-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_alter_apointment_time_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='day',
            field=models.CharField(blank=True, max_length=155, verbose_name='day'),
        ),
    ]
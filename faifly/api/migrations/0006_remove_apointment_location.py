# Generated by Django 4.0.5 on 2022-06-26 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_apointment_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apointment',
            name='location',
        ),
    ]

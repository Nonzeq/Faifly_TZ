# Generated by Django 4.0.5 on 2022-06-26 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_remove_apointment_range'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range_time', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.apointment', verbose_name='RANGE')),
            ],
        ),
    ]
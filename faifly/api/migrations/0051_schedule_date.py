# Generated by Django 4.0.5 on 2022-06-27 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_alter_schedule_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]

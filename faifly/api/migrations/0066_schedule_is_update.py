# Generated by Django 4.0.5 on 2022-07-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0065_remove_schedule_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='is_update',
            field=models.BooleanField(default=False),
        ),
    ]